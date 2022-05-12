<template>
  <ui-list :type="2">
    <ui-item v-for="expense in expenses" :key="expense.id">
      <ui-item-first-content>
        <ui-icon>attach_money</ui-icon>
        {{ expense.amount }}
      </ui-item-first-content>

      <ui-item-text-content>
        <ui-item-text1>{{ expense.name }}</ui-item-text1>
        <ui-item-text2>{{ expense.category.name }}</ui-item-text2>
      </ui-item-text-content>
      <ui-item-last-content>
        <ui-icon-button icon="density_small"></ui-icon-button>
      </ui-item-last-content>
    </ui-item>
  </ui-list>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "ExpenseList",
  computed: {
    ...mapGetters([
      'expenses',
    ])
  }
}
</script>

<style scoped>

</style>
