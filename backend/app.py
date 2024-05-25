from logic.analytics_collector import AnalyticsCollector
from logic.order_creator import OrderCreator
from logic.order_mediator import OrderMediator
from logic.order_parser import OrderParser
from logic.order_notifier import OrderNotifier
from logic.kitchen_observer import KitchenObserver
from logic.waiter_observer import WaiterObserver

from db.db_access import DBAccess

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

db_access = DBAccess()
analytics_collector = AnalyticsCollector(db_access=db_access)
order_creator = OrderCreator()
order_parser = OrderParser()
order_notifier = OrderNotifier()
kitchen_observer = KitchenObserver()
order_notifier.subscribe(notify_type="ready_to_cook", observer=kitchen_observer)

order_mediator = OrderMediator(order_parser=order_parser, 
                                order_creator=order_creator,
                                order_notifier=order_notifier,
                                analytics_collector=analytics_collector)

order_creator.set_mediator(order_mediator=order_mediator)
order_parser.set_mediator(order_mediator=order_mediator)

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/api/login/<username>/<password>")
def authenticate_user(username, password):
    db_access.connect()

    query = "SELECT Username FROM account WHERE Username=%s AND PassWord=%s"
    values = (username, password)

    result = db_access.make_query(query=query, values=values)

    if result and len(result) == 1:
        data = {
            "username": result[0][0]
        }
        return jsonify(data), 200

    data = {
        "err": "couldn't find an exact match for your credentials"
    }
    return jsonify(data), 404

@app.route("/api/reservation/create", methods=['POST'])
def create_reservation():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be in JSON format"}), 400

    db_access.connect()
    conn = db_access.retrieve_connection()
    cursor = conn.cursor()

    return_data = {}

    try:
        conn.start_transaction()
        query = "INSERT INTO reservation (ResDate, ResTime, attendees) VALUES (%s, %s, %s)"
        structured_res_date = datetime.strptime(data["reservationDate"], "%d-%m-%Y")
        values = (structured_res_date, data["resTime"], data["attendees"])
        cursor.execute(query, values)
        reservation_id = cursor.lastrowid
        conn.commit()
        db_access.disconnect()
        return_data["reservation_id"] = reservation_id
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

    return jsonify(return_data), 200

@app.route("/api/reservation/delete", methods=['DELETE'])
def delete_reservation():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be in JSON format"}), 400

    db_access.connect()
    conn = db_access.retrieve_connection()
    cursor = conn.cursor()

    try:
        conn.start_transaction()
        query = "DELETE FROM reservation WHERE ReservationID = %s"
        values = [data["reservationId"]]
        cursor.execute(query, values)
        conn.commit()
        db_access.disconnect()
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

    return jsonify({"success": "Reservation deleted"}), 200

@app.route("/api/reservation/<reservation_id>")
def get_reservation(reservation_id):
    db_access.connect()
    conn = db_access.retrieve_connection()
    cursor = conn.cursor()

    response_data = None

    try:
        conn.start_transaction()
        query = "SELECT * FROM reservation WHERE ReservationID = %s"
        values = [reservation_id]
        cursor.execute(query, values)
        response_data = cursor.fetchall()
        conn.commit()
        db_access.disconnect()
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

    if not response_data:
        return jsonify({"error": "Reservation not found"}), 404

    reservation_date = response_data[0][1].strftime("%d-%m-%Y")
    return_data = {
        "id": response_data[0][0],
        "reservationDate": reservation_date,
        "reservationTime": response_data[0][2],
        "attendees": response_data[0][3]
    }
    return jsonify(return_data), 200

@app.route("/api/reservation/all")
def get_all_reservations():
    db_access.connect()
    conn = db_access.retrieve_connection()
    cursor = conn.cursor()

    response_data = None

    try:
        conn.start_transaction()
        query = "SELECT * FROM reservation"
        cursor.execute(query)
        response_data = cursor.fetchall()
        conn.commit()
        db_access.disconnect()
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

    if not response_data:
        return jsonify({"error": "Reservation not found"}), 404

    adjusted_data = {
        "reservations": []
    }

    for reservation in response_data:
        reservation_date = reservation[1].strftime("%d-%m-%Y")
        reservation_adjusted = {
            "id": reservation[0],
            "reservationDate": reservation_date,
            "reservationTime": reservation[2],
            "attendees": reservation[3]
        }
        adjusted_data["reservations"].append(reservation_adjusted)

    return jsonify(adjusted_data), 200


@app.route("/api/menu/create-item", methods=["POST"])
def create_menu_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be in JSON format"}), 400

    db_access.connect()
    conn = db_access.retrieve_connection()
    cursor = conn.cursor()

    try:
        conn.start_transaction()
        query = "INSERT INTO menuitem (Name, Description, Price, NutritionInfo, MenuStatus) VALUES (%s, %s, %s, %s, 1)"
        values = [data['name'], data['description'], data['price'], data['nutritionInfo']]
        cursor.execute(query, values)
        conn.commit()
        db_access.disconnect()
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

    return jsonify({"success": "Item added"}), 200

@app.route("/api/menu/get-menu")
def get_full_menu():
    db_access.connect()
    conn = db_access.retrieve_connection()
    cursor = conn.cursor()

    data = {
        "menu": []
    }

    try:
        conn.start_transaction()
        query = "SELECT * FROM menuitem"
        cursor.execute(query)
        response_data = cursor.fetchall()
        for menu_item in response_data:
            currently_on_menu = lambda x: True if x == 1 else False
            item = {
                "id": menu_item[0],
                "name": menu_item[1],
                "description": menu_item[2],
                "price": menu_item[3],
                "nutritionInfo": menu_item[4],
                "onMenu": currently_on_menu(menu_item[5])
            }
            data["menu"].append(item)

        conn.commit()
        db_access.disconnect()
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

    return jsonify(data), 200

@app.route("/api/menu/remove-item-from-active-menu", methods=["PUT"])
def remove_item_from_active_menu():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be in JSON format"}), 400

    db_access.connect()
    conn = db_access.retrieve_connection()
    cursor = conn.cursor()

    try:
        conn.start_transaction()
        query = "UPDATE menuItem SET MenuStatus = 0 WHERE MenuItemID = %s"
        values = [data["menuItem"]]
        cursor.execute(query, values)
        conn.commit()
        db_access.disconnect()
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

    return jsonify({"success": "Menu Item updated"}), 200

@app.route("/api/menu/add-item-to-active-menu", methods=["PUT"])
def add_item_to_active_menu():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be in JSON format"}), 400

    db_access.connect()
    conn = db_access.retrieve_connection()
    cursor = conn.cursor()

    try:
        conn.start_transaction()
        query = "UPDATE menuItem SET MenuStatus = 1 WHERE MenuItemID = %s"
        values = [data["menuItem"]]
        cursor.execute(query, values)
        conn.commit()
        db_access.disconnect()
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

    return jsonify({"success": "Menu Item updated"}), 200

@app.route("/api/order/create", methods=["POST"])
def create_order():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be in JSON format"}), 400

    try:
        order = order_creator.create_order(data)
        order_mediator.process_order(order)
        return jsonify({"success": "Order was created"}), 200
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

@app.route("/api/kitchen/display")
def kitchen_display():
    try:
        orders = kitchen_observer.get_orders()
        return jsonify({"orders": orders}), 200
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

@app.route("/api/kitchen/update-status", methods=["POST"])
def update_order_status():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be in JSON format"}), 400

    order_id = data.get('order_id')
    status = data.get('status')

    try:
        kitchen_observer.update_order_status(order_id, status)
        return jsonify({"success": "Order status updated"}), 200
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500


@app.route("/api/waiter/display")
def waiter_display():
    try:
        orders = waiter_observer.get_orders()
        return jsonify({"orders": orders}), 200
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

@app.route("/api/analytics", methods=["GET"])
def get_analytics():
    try:
        analytics_data = analytics_collector.collect()
        return jsonify(analytics_data), 200
    except Exception as e:
        print("ERROR HAS OCCURRED: ", e)
        return jsonify({"err": "We had an error with the server"}), 500

if __name__ == "__main__":
    app.run(debug=True)
