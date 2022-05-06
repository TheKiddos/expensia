import Vue from 'vue';

import BalmUI from 'balm-ui'; // Official Google Material Components
import BalmUIPlus from 'balm-ui/dist/balm-ui-plus'; // BalmJS Team Material Components

Vue.use(BalmUI); // Mandatory
Vue.use(BalmUIPlus); // Optional

import store from './store'
import App from '@/views/layouts/app';

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  store,
  components: { App },
  template: '<app/>'
});
