app.component('app-bar',
	{
		data() {
			return {
				isNavbarOpen: false,
				websiteTitle: 'Relaxing Koala',
				navLinks: [
					{ text: 'View Menu', route: './menu-view-display.html' },
					{ text: 'Edit Menu', route: './menu-edit-display.html' },
					{ text: 'Kitchen Display', route: './kitchen-display.html' },
					{ text: 'Waiter Display', route: './waiter-display.html' },
					{ text: 'Reservations', route: './reservation-display.html' },
					{ text: 'Analytics', route: './analytics.html' }
				]
			};
		},
		methods: {
			toggleNavbar() {
				this.isNavbarOpen = !this.isNavbarOpen;
			}
		},
		template: `
			<nav class="navbar navbar-expand-md navbar-dark bg-primary">
				<div class="container-fluid">
				<a class="navbar-brand" href="#">{{ websiteTitle }}</a>
				<button class="navbar-toggler" type="button" @click="toggleNavbar" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>

				<div class="collapse navbar-collapse" :class="{ 'show': isNavbarOpen }" id="navbarSupportedContent">
					<ul class="navbar-nav ml-auto">
					<li class="nav-item" v-for="link in navLinks" :key="link.text">
						<a :href="link.route" class="nav-link">{{ link.text }}</a>
					</li>
					</ul>
				</div>
				</div>
			</nav>
		`
	});

