<template>
  <div class = "row" >
    <div class = "col m-md-auto " >
      <h2 class = "text-center" >Introduction of Production</h2 >
      <table class = "table table-bordered table-striped p-sm-5 " >
        <thead >
        <tr class = "text-color: #2c3e50">
          <th bgcolor="#00ffff">No</th >
          <th bgcolor="#ffdab9">Product name</th >
          <th bgcolor="#adff2f" class = "text-md-center " >Production company</th >
          <th bgcolor="#9932cc" class = "text-md-center" >Country of origin</th >
          <th bgcolor="#4932cc" class = "text-md-center" >Description</th >
          <th bgcolor="#d932cc" class = "text-md-center" >Review</th >
        </tr >
        </thead >
        <tbody >
        <tr v-if = "products.length == 0" >
          <td bgcolor="#ffd700" colspan = "6" class = "text-center" >
            Your record is empty
          </td >
        </tr >
        <tr v-for="product in products" @click="selectProduct(product)">
          <td bgcolor="#00ffff">{{product.id}}</td>
          <td bgcolor="#ffdab9">{{product.category}}</td>
          <td bgcolor="#adff2f">{{product.quantity}}</td>
          <td bgcolor="#9932cc">{{product.description}}</td>
          <td bgcolor="#4932cc">{{product.sellPrice}}</td>
          <td bgcolor="#d932cc">{{product.buyPrice}}</td>
        </tr>
        </tbody>
      </table >
    </div >
  </div >
</template>

<script>
  import {APIService} from '../../http/APIService'
  const apiService = new APIService()
  export default {
    name: 'HistoricalRecord',
    data () {
      return {
        selectedProduct: null,
        products: [],
        numberOfPages: 0,
        pages: [],
        numberOfProduct: 0,
        loading: false,
        nextPageURL: '',
        previousPageURL: '',
        selectedIndex: -1
      }
    },
    methods: {
      getProducts () {
        this.loading = true
        apiService.getProducts().then((page) => {
          this.products = page.data
          this.numberOfProducts = page.count
          this.numberOfPages = page.numpages
          this.nextPageURL = page.nextlink
          this.previousPageURL = page.prevlink
          if (this.numberOfPages) {
            for (var i = 1; i <= this.numberOfPages; i++) {
              const link = `/api/products/?page=${i}`
              this.pages.push({pageNumber: i, link: link})
            }
          }
          this.loading = false
        })
      },
      selectProduct (product) {
        this.selectedProduct = product
      }
    },
    created () {
      this.getProducts()
    }
  }
</script>

<style scoped>

</style>
