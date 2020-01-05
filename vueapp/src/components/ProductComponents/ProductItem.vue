<template>
  <div class="col-md-2">
    <div class="card">
      <img :src="image" :alt="name" class="card-img-top">
      <div class="card-body">
        <h4 class="card-title">{{ name }}</h4>
        <div class="card-text">${{ price | dollars }}</div>
        <div class="row justify-content-end">
          <button class="btn btn-danger" @click="addToCart(invId)">Add to cart</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'Product',
    props: ['invId', 'name', 'image', 'price'],
    filters: {
      dollars: num => `$${num / 100}`
    },
    methods: {
      addToCart (invId) {
        this.$store.dispatch('addToCart', invId)
      }
    }
  }
</script>
