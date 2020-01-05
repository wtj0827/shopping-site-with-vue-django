<template>
  <div class = "row">
    <div class = "col m-md-auto text-center">
      <h3 style="margin-top: 50px; border-left: 20px; margin-left: 0px; background-color: yellow; color: gray">
        &nbsp;&nbsp;Let's ensure maximum sincerity and kindness in customer service!
      </h3>
      <h3 class = "text-center" >Delivery State ({{numberOfProducts}})</h3 >
      <div class="row">
        <div class="w3-col m3"></div>
        <div class="w3-col m6">
          <table class="w3-table-all w3-tiny"
                 style="border-left-width: 0px; padding-left: 0px; margin-top: 10px; border-right-width: 0px; text-align: center;">
            <thead>
            <tr class="w3-light-grey w3-hover-red w3-text-green" style="font-size: 16px;">
              <th>No</th >
              <th>User name</th >
              <th>Product name</th >
              <th>Sale Price</th >
              <th>Quantity</th >
              <th>Delivery address</th >
              <th>Seller Name</th >
              <th>Delivery State</th >
            </tr >
            </thead >
            <tbody >
            <tr v-if = "products.length == 0" >
              <td bgcolor="#ffd700" colspan = "6" class = "text-center" >
                Your record is empty
              </td >
            </tr >
            <tr class="w3-text-cyan w3-hover-blue-grey" style="font-size: 12px;" v-for="product in products" @click="selectProduct(product)">
              <td>{{product.id}}</td>
              <td>{{product.category}}</td>
              <td>{{product.quantity}}</td>
              <td>{{product.description}}</td>
              <td>{{product.sellPrice}}</td>
              <td>{{product.buyPrice}}</td>
              <td>{{product.sku}}</td>
              <td>{{product.unit}}</td>
            </tr>
            </tbody>
          </table >
        </div>
      </div>
      <a href="/Sellers-List" class="active w3-hover-text-light-green w3-text-red">&nbsp;Sellers List &nbsp;</a>
      <a href="/Historical-Record" class="active w3-hover-text-light-green w3-text-red">&nbsp;Historical-Record&nbsp;</a>
      <a href="/Delivery-State" class="active w3-hover-text-light-green w3-text-red">&nbsp;Delivery-State&nbsp;</a>
      <a href="/Product-list" class="active w3-hover-blue-grey w3-text-green">&nbsp;back&nbsp;</a>
    </div >
  </div >
</template>

<script>
  import {APIService} from '../../http/APIService'
  const apiService = new APIService()
  export default {
    name: 'DeliveryState',
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
