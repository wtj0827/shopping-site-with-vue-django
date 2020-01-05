<template>
  <div>
    <button class="btn btn-danger" data-toggle="modal" data-target="#shoppingCart">Cart ({{ numInCart }})</button>
  </div>
</template>
<script>
  export default {
    name: 'shoppingCart',
    computed: {
      inCart () {
        return this.$store.getters.inCart
      },
      numInCart () {
        return this.inCart.length
      }
    }
  }
</script>
<style>
  #shoppingCart {
    top: 40px;
    display: block;
  }
</style>
