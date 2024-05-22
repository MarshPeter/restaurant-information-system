import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import vuetifyConfig from '../../vuetify.config.js'; // Import your Vuetify config

const vuetify = createVuetify({
  components,
  directives,
  ...vuetifyConfig, // Spread your Vuetify config
});

export default vuetify;