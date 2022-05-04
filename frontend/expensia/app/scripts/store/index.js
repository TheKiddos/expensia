// No need for modules since this is a simple app

import Vuex from 'vuex'
import Vue from 'vue';
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    expenses: [
      {
        id: 1,
        name: 'wife',
        amount: 2000,
        category: 1,
        created: '2022-12-2',
      },
      {
        id: 2,
        name: 'country',
        amount: 20,
        category: 2,
        created: '2022-12-2',
      },
    ],
  },
  mutations: {},
})

export default store;
