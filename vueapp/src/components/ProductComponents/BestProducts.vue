<template>
<div style="margin: 30px 20px">
  <h1 id="bestProduct-header">Best Products</h1>
  <div class="row mb-3">
      <div class="col-md-11">
      </div>
      <div class="col-md-1">
        <ShoppingCart />
      </div>
    </div>
  <div class="row">
    <Product
        v-for="item in forSale"
        :key="item.invId"
        :invId="item.invId"
        :name="item.name"
        :image="item.image"
        :price="item.price" />
  </div>
</div>
</template>

<script>
/* eslint-disable */
import {APIService} from '../../http/APIService'
import Loading from '../Loading'
import Product from './ProductItem.vue'
import ShoppingCart from './ShoppingCart.vue'
const API_URL = 'http://localhost:8000'
const apiService = new APIService()

export default {
  name: 'BestProducts',
  components: {
    Loading,
    Product,
    ShoppingCart
  },
  data() {
    return {
      selectedProduct:null,
      products: [],
      numberOfPages:0,
      pages : [],
      numberOfProducts:0,
      loading: false,
      nextPageURL:'',
      previousPageURL:''
    };
  },
  methods: {
    getProducts(){

      this.loading = true;
      apiService.getProducts().then((page) => {
        this.products = page.data;

        this.numberOfProducts = page.count;
        this.numberOfPages = page.numpages;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        if(this.numberOfPages)
        {
          for(var i = 1 ; i <= this.numberOfPages ; i++)
          {
            const link = `/api/products/?page=${i}`;
            this.pages.push({pageNumber: i , link: link})
          }
        }
        this.loading = false;
      });
    },
    getPage(link){
      this.loading = true;
      apiService.getProductsByURL(link).then((page) => {
        this.products = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        this.loading = false;
      });
    },
    getNextPage(){
      this.loading = true;
      apiService.getProductsByURL(this.nextPageURL).then((page) => {
        this.products = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        this.loading = false;
      });

    },
    getPreviousPage(){
      this.loading = true;
      apiService.getProductsByURL(this.previousPageURL).then((page) => {
        this.products = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        this.loading = false;
      });

    },
    deleteProduct(product){
      apiService.deleteProduct(product).then((r)=>{
        if(r.status === 204)
        {
          /*for(var i = this.products.length-1; i--;){
            console.log(this.products[i].pk);
            if (this.products[i].pk === product.pk)
            {
              console.log("deleting product " + this.products[i].pk)
              this.products.splice(i, 1);
            }
          }*/
          alert("Product deleted");
          this.$router.go()

        }
      })
    },
    selectProduct(product){
      this.selectedProduct = product;
    }
  },
  mounted() {
    this.getProducts();
  },

  computed: {
    forSale() { return this.$store.getters.forSale; },
    inCart() { return this.$store.getters.inCart; },
  }
}
</script>
<style scoped>
#bestProduct-header {
  color: #a29b9b;
  padding-bottom: 10px;
  border-bottom: 3px solid #a29b9b;
  font-size: 40px;
  font-family: fantasy;
}

.list-horizontal li {
	display:inline-block;
}
.list-horizontal li:before {
	content: '\00a0\2022\00a0\00a0';
	color:#999;
	color:rgba(0,0,0,0.5);
	font-size:11px;
}
.list-horizontal li:first-child:before {
	content: '';
}
</style>
