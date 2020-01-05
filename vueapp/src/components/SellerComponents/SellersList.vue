<!-- This page is shown
---- the list of sellers-->
<!--auther: KYG_2019/12/25-->

<template>
  <div>
    <div class="col mt-2 container-fluid text-center">
      <h3 class="w3-text-yellow" style="margin-top: 50px; background-color:dodgerblue;">
        Let's ensure maximum sincerity and kindness in customer service!
      </h3>
      <div class="w3-row">
        <div class="w3-col m6">
          <div class="w3-row-padding w3-margin-top">
            <div class="w3-third">
              <div class="w3-card">
                <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-21.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
                     onclick="document.getElementById('modal01').style.display='block'">
                <div id="modal01" class="w3-modal" onclick="this.style.display='none'">
                  <span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
                  <div class="w3-modal-content w3-animate-zoom">
                    <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-21.jpg')" style="width:100%">
                  </div>
                </div>
                <div class="w3-container w3-2018-red-pear">
                  <h5>Terre</h5>
                </div>
              </div>
            </div>
            <div class="w3-third">
              <div class="w3-card">
                <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-22.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
                     onclick="document.getElementById('modal02').style.display='block'">
                <div id="modal02" class="w3-modal" onclick="this.style.display='none'">
                  <span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
                  <div class="w3-modal-content w3-animate-zoom">
                    <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-22.jpg')" style="width:100%">
                  </div>
                </div>
                <div class="w3-container w3-2018-nebulas-blue">
                  <h5>Monterosso</h5>
                </div>
              </div>
            </div>
            <div class="w3-third">
              <div class="w3-card">
                <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-27.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
                     onclick="document.getElementById('modal03').style.display='block'">
                <div id="modal03" class="w3-modal" onclick="this.style.display='none'">
                  <span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
                  <div class="w3-modal-content w3-animate-zoom">
                    <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-27.jpg')" style="width:100%">
                  </div>
                </div>
                <div class="w3-container w3-2018-ultra-violet">
                  <h5>Vernazza</h5>
                </div>
              </div>

            </div>
            <div class="w3-col m6">

            </div>
          </div>
        </div>
        <div class="w3-col m6">
          <div class="w3-row-padding w3-margin-top">
            <div class="w3-third">
              <div class="w3-card w3-animate-zoom">
                <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-24.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
                     onclick="document.getElementById('modal04').style.display='block'">
                <div id="modal04" class="w3-modal" onclick="this.style.display='none'">
                  <span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
                  <div class="w3-modal-content w3-animate-zoom">
                    <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-24.jpg')" style="width:100%">
                  </div>
                </div>
                <div class="w3-container w3-2018-cherry-tomato">
                  <h5>Manarola</h5>
                </div>
              </div>
            </div>

            <div class="w3-third">
              <div class="w3-card">
                <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-25.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
                     onclick="document.getElementById('modal05').style.display='block'">
                <div id="modal05" class="w3-modal" onclick="this.style.display='none'">
                  <span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
                  <div class="w3-modal-content w3-animate-zoom">
                    <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-25.jpg')" style="width:100%">
                  </div>
                </div>
                <div class="w3-container w3-2018-arcadia">
                  <h5>Corniglia</h5>
                </div>
              </div>
            </div>

            <div class="w3-third">
              <div class="w3-card">
                <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-26.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
                     onclick="document.getElementById('modal06').style.display='block'">
                <div id="modal06" class="w3-modal" onclick="this.style.display='none'">
                  <span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
                  <div class="w3-modal-content w3-animate-zoom">
                    <img class="w3-hover-opacity" :src="require('@/assets/seller/seller-26.jpg')" style="width:100%">
                  </div>
                </div>
                <div class="w3-container w3-2018-lime-punch">
                  <h5>Riomaggiore</h5>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="w3-row">
        <div v-if="!selectedProduct" class="w3-col m6">
          <div class="w3-row">
            <div id="w3-container" style="margin-top: 17px">
              <carousel :per-page="1" :mouse-drag="true" :autoplay="true" :autoplayTimeout="1500"
                        :loop="true">
                <slide>
                  <img :src="require('@/assets/seller/SellerList_show1.jpg')" alt="Chicago" width="80%"
                       height="600">
                </slide>
                <slide>
                  <img :src="require('@/assets/seller/SellerList_show2.jpg')" alt="Chicago" width="80%"
                       height="600">
                </slide>
                <slide>
                  <img :src="require('@/assets/seller/SellerList_show3.jpg')" alt="Chicago" width="80%"
                       height="600">
                </slide>
              </carousel>
            </div>
          </div>
        </div>
        <div v-else="selectedProduct" class="w3-col m6">
          <div class="w3-container w3-padding-64 w3-theme-l5" style="margin-left: 150px" id="contact">
            <div class="w3-row" style="height: 450px; "><br><br><br>
              <div class="w3-col m5">
                <div class="w3-padding-16"><span class="w3-xlarge w3-border-teal w3-bottombar">Contact the other seller</span></div>
                <h3>Address</h3>
                <p>Welcome to visit our site !</p>
                <p><i class="fa fa-map-marker w3-text-teal w3-xlarge"></i>  Chicago, US</p>
                <p><i class="fa fa-phone w3-text-teal w3-xlarge"></i>  +00 1515151515</p>
                <p><i class="fa fa-envelope-o w3-text-teal w3-xlarge"></i>  test@test.com</p>
              </div>
              <div class="w3-col m7">
                <form class="w3-container w3-card-4 w3-padding-16 w3-white" action="/product-list" target="_blank">
                  <div class="w3-section">
                    <label>Name</label>
                    <input class="w3-input" type="text" name="Name" required>
                  </div>
                  <div class="w3-section">
                    <label>Email</label>
                    <input class="w3-input" type="text" name="Email" required>
                  </div>
                  <div class="w3-section">
                    <label>Message</label>
                    <input class="w3-input" type="text" name="Message" required>
                  </div>
                  <input class="w3-check" type="checkbox" checked name="Like">
                  <label>I Like it!</label>
                  <button type="submit" class="w3-button w3-right w3-theme">Send</button>
                </form>
              </div>
            </div>
          </div>
        </div>
        <div class="w3-col m5 w3-border w3-container w3-margin">
          <h2 class="text-center w3-text-teal"> Sellers List (<a class="w3-text-red"> {{numberOfProducts}}</a>)</h2>
          <table class="table w3-text-blue table-bordered table-striped p-2 text-center">
            <thead>
            <tr class="text-color: #2c3e50 text-center  w3-hover-blue-grey">
              <th bgcolor="#808f9fd5f9ff">No</th>
              <th bgcolor="#d5f9ff">Name</th>
              <th bgcolor="#b0bf9f">Gender</th>
              <th bgcolor="#baa02f">Birthday</th>
              <th bgcolor="#70f5ff">Address</th>
              <th bgcolor="#99ffcc">Years</th>
              <th bgcolor="#e0ffbc">Review</th>
            </tr>
            </thead>
            <tbody>
            <tr class="w3-text-cyan w3-hover-blue-grey" v-for="product in products" @click="selectProduct(product)">
              <td bgcolor="#808f9f">{{product.id}}</td>
              <td bgcolor="#d5f9ff">{{product.category}}</td>
              <td bgcolor="#b0bf9f">{{product.sellPrice}}</td>
              <td bgcolor="#baa02f">{{product.quantity}}</td>
              <td bgcolor="#70f5ff">{{product.description}}</td>
              <td bgcolor="#99ffcc">{{product.sku}}</td>
              <td bgcolor="#e0ffbc"> Star {{product.review}}</td>
            </tr>
            </tbody>
          </table>
          <a href="/Sellers-List" class="active w3-text-yellow w3-hover-green">&nbsp;Sellers List &nbsp;</a>
          <a href="/Historical-Record" class="active w3-text-yellow w3-hover-green">&nbsp;Historical-Record&nbsp;</a>
          <a href="/Delivery-State" class="active w3-text-yellow w3-hover-green">&nbsp;Delivery-State&nbsp;</a>
          <a href="/Product-list" class="active w3-text-red w3-hover-green">&nbsp;back&nbsp;</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {APIService} from '../../http/APIService'

  const apiService = new APIService()
  export default {
    name: 'SellersList',
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
