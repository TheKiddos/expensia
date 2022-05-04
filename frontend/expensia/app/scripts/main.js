import Vue from 'vue';

import store from './store'
import App from '@/views/layouts/app';

Vue.config.productionTip = false;

new Vue({
  el: '#app',
  store,
  components: { App },
  template: '<app/>'
});
