<template>
  <div>
    <TheHeader></TheHeader>
    <main class="container">
      <home-dashboard></home-dashboard>
    </main>
  </div>
</template>

<script>
import TheHeader from './TheHeader';
import HomeDashboard from '@/views/pages/HomeDashboard';

export default {
  name: 'App',
  components: {
    TheHeader,
    HomeDashboard
  },
  data() {
    return {

    };
  }
};
</script>
