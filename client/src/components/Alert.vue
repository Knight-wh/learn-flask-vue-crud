<template>
  <div>
    <div class="alert alert-dismissible fade show" :class="alertStyle" role="alert">
      {{ message }}
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    <br/>
  </div>
</template>

<script>
export default {
  props: ['message','type'],
  computed: {
    alertStyle() {
      return `alert-${this.type}`;
    }
  }
};
</script>
