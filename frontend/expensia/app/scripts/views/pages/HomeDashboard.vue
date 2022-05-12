<template>
  <div>
    <h1 class="page-title">Dashboard</h1>
    <expense-list></expense-list>
  </div>
</template>

<script>
import ExpenseList from '@/views/components/expense/ExpenseList';

export default {
  name: "HomeDashboard",
  components: {
    ExpenseList,
  },
}
</script>

<style scoped>

</style>
