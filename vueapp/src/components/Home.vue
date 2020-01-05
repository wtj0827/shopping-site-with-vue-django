<template>
<main role="main">
    <div id="main-container">
      <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplayTimeout="2000" :loop="true">
          <slide>
              <img :src="require('@/assets/slide-01.jpg')" alt="Chicago" width="100%" height="600">
          </slide>
          <slide>
              <img :src="require('@/assets/slide-03.jpg')" alt="Chicago" width="100%" height="600">
          </slide>
          <slide>
              <img :src="require('@/assets/slide-02.jpg')" alt="Chicago" width="100%" height="600">
          </slide>
      </carousel>
    </div>
    <BestProducts></BestProducts>
</main>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel'
import BestProducts from './ProductComponents/BestProducts.vue'

/* eslint-disable */
  export default {
    name: 'home',
    components: {
      Carousel,
      Slide,
      BestProducts
    },
    props: ['auth', 'authenticated'],
    data(){
        return {
          access_token: localStorage.getItem('access_token'),
          id_token: localStorage.getItem('id_token'),
          profile: {}
        }
    },
    methods:{
      getUserProfile(){
        this.auth.getUserProfile((err, profile)=> {
          if(err) return null
          this.profile = profile
        });
      }
    },

  mounted(){
    this.getUserProfile()
  }
  }
</script>

<style>
  #main-container {
    min-height: 80%;
    padding-top: 40px;
    width: 100%;
    background-color: #222;
  }
  a {
    cursor: pointer;
  }
</style>
