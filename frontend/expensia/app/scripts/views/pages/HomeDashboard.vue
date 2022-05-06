<template>
  <div>
    <h1 class="page-title">Dashboard</h1>
    <ui-list>
      <ui-item v-for="i in 3" :key="i">
        <ui-item-text-content>Line item</ui-item-text-content>
      </ui-item>
    </ui-list>
  </div>
</template>

<script>
export default {
  name: "HomeDashboard"
}
</script>

<style scoped>

</style>
