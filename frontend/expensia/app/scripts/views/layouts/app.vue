<template>
  <div>
    <TheHeader></TheHeader>
    <div class="container">
      <header class="hero">
      </header>
    </div>
  </div>
</template>

<script>
import TheHeader from '@/views/layouts/TheHeader';

export default {
  name: 'App',
  components: {
    TheHeader
  },
  data() {
    return {

    };
  }
};
</script>
