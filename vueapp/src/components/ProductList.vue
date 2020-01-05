<template>
	<div class="bg-transparent text-justify">
		<h6 style="margin-top: 40px; border: 40px; background-color:MediumSeaGreen; text-align: center">
			<h3 class="w3-text-yellow w3-hover-text-brown"> Brief introduction of the product (<a class="w3-text-red">{{numberOfProducts}}</a>)
			</h3>
			<a href="/Sellers-List" class="w3-hover-border-green w3-hover-green w3-text-yellow">&nbsp;Sellers List
				&nbsp;</a>
			<a href="/Historical-Record" class="w3-hover-border-green w3-hover-green w3-text-yellow">&nbsp;Historical-Record&nbsp;</a>
			<a href="/Delivery-State" class="w3-hover-border-green w3-hover-green w3-text-yellow">&nbsp;Delivery-State&nbsp;</a>
		</h6>
		<Loading :loading="loading"></Loading>
<!-- Start modifying: KYG_2019/12/24-->

		<div class="w3-row">
<!--  Selecting the categories-->
			<div class="w3-col s2 m2 l2">
				<div class="w3-container w3-hover-blue-gray w3-theme-dark">
					<section>
						<div class="condition-render-verticalFilters condition-render-boundary-top" style="top: 0px; bottom: auto;">
							<div class="vertical-filters-filters header-container">
								<span class="header-title mdl-color-text--blue-400">
									<br>
									<h6 class="w3-bar-item w3-button w3-teal">Select the attributes of the product <br>you want to buy</h6>
									<br>
								</span>
							</div>
<!--  Selecting the Gender-->
							<div class="vertical-filters-filters header-container">
								<span class="header-title mdl-color-text--blue-400">
									<h6 class="table-hover">Gender</h6>
								</span>
								<div class="vertical-filters-filters" v-model="selectedGenderIndex">
									<ul class="gender-list">
										<li><label class="common-customCheckbox gender-label undefined"><input type="checkbox" v-model="genderMale" value="male" v-on:change="filterGenderTable()">Male</label></li>
										<li><label class="common-customCheckbox gender-label"><input type="checkbox" v-model="genderFemale" value="Female" v-on:change="filterGenderTable()">Female</label></li>
										<li><label class="common-customCheckbox gender-label"><input type="checkbox" v-model="genderBoy" value="boy" v-on:change="filterGenderTable()">Boy</label></li>
										<li><label class="common-customCheckbox gender-label"><input type="checkbox" v-model="genderGirl" value="girl" v-on:change="filterGenderTable()">Girl</label></li>
									</ul>
								</div>
							</div>
<!--Selecting of categories-->
							<div class="vertical-filters-filters categories-container">
								<span class="vertical-filters-header mdl-color-text--blue-400">
					<h6 class="table-hover">Categories</h6>
				</span>
								<div class="filter-search-filterSearchBox">
									<input type="text" class="text-center filter-search-inputBox filter-search-hidden bg-warning"
										   placeholder="Search for Categories">
									<span class="myntraweb-sprite filter-search-iconSearch sprites-search"></span>
								</div>
								<ul class="categories-list">
									<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox" v-model="categoryTshirts"
																										   value="tshirts" v-on:change="filterCategoryTable()">
										Tshirts
									</label></li>
									<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox" v-model="categoryShoes"
																										   value="shoes" v-on:change="filterCategoryTable()">
										Shoes
									</label></li>
									<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox" v-model="categoryJeans"
																										   value="jeans" v-on:change="filterCategoryTable()">
										Jeans
									</label></li>
									<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox" v-model="categoryTrousers"
																										   value="trousers" v-on:change="filterCategoryTable()">
										Trousers
									</label></li>
									<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox" v-model="categoryJackets"
																										   value="jackets" v-on:change="filterCategoryTable()">
										Jackets
									</label></li>
									<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox" v-model="categorySportsShoes"
																										   value="sportsShoes" v-on:change="filterCategoryTable()">
										Sports Shoes
									</label></li>
								</ul>
							</div>
<!--Selecting of color-->
							<div class="vertical-filters-filters categories-container">
								<span class="vertical-filters-header mdl-color-text--blue-400">
									<h6 class="table-hover">Color</h6>
								</span>

								<div class="filter-search-filterSearchBox">
									<input type="text" class="text-center filter-search-inputBox filter-search-hidden bg-warning"
										   placeholder="Search for Color">
									<span class="myntraweb-sprite filter-search-iconSearch sprites-search"></span>
								</div>
								<ul class="categories-list">
									<li><label class="common-customCheckbox vertical-filters-label">
										<input type="checkbox" v-model="colorRed" value="red" v-on:change="filterColorTable()">
										Red
									</label></li>
									<li><label class="common-customCheckbox vertical-filters-label">
										<input type="checkbox" v-model="colorGreen" value="green" v-on:change="filterColorTable()">
										Green
									</label></li>
									<li><label class="common-customCheckbox vertical-filters-label">
										<input type="checkbox" v-model="colorBlack" value="black" v-on:change="filterColorTable()">
										Black
									</label></li>
									<li><label class="common-customCheckbox vertical-filters-label">
										<input type="checkbox" v-model="colorBlue" value="blue" v-on:change="filterColorTable()">
										Blue
									</label></li>
									<li><label class="common-customCheckbox vertical-filters-label">
										<input type="checkbox" v-model="colorYellow" value="yellow" v-on:change="filterColorTable()">
										Yellow
									</label></li>
								</ul>
							</div>
<!--Selecting of price-->
							<div class="vertical-filters-filters">
								<span class="vertical-filters-header mdl-color-text--blue-400">
									<h6 class="table-hover">Price</h6>
								</span>
								<ul class="price-list">
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="price" value="50"  v-on:change="filterPriceTable()">50$ or less
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="price" value="100" v-on:change="filterPriceTable()">51$ to 100$
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="price" value="500" v-on:change="filterPriceTable()">101$ to 500$
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="price" value="2000" v-on:change="filterPriceTable()">501$ to 2000$
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="price" value="2001" v-on:change="filterPriceTable()">2001$ or more
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="price" value="0" v-on:change="filterPriceTable()">None
									</label></li>
								</ul>
							</div>
<!--Selecting of Payment method-->
							<div class="vertical-filters-filters">
				<span class="vertical-filters-header mdl-color-text--blue-400">
					<h6 class="table-hover">Payment method</h6>
				</span>
								<ul class="payment-list">
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" class="Payment-method" name="Payment-method"
											   value="Electronic payment card">Electronic
										payment
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" class="Payment-method" name="Payment-method" value="money">money
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" class="Payment-method" name="Payment-method"
											   value="Payment after delivery">Payment
										after delivery
									</label></li>
								</ul>
							</div>
<!--Selecting of discount range-->
							<div class="vertical-filters-filters">
								<span class="vertical-filters-header mdl-color-text--blue-400">
									<h6 class="table-hover">Discount Range</h6>
								</span>
								<ul class="discount-list">
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" class="discount-input" v-model="discountRange" value="10" v-on:change="filterDiscountRangeTable()">
										10% and above
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="discountRange" value="20" v-on:change="filterDiscountRangeTable()">20% and above
<!--										<div class="common-radioIndicator"></div>-->
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="discountRange" value="30" v-on:change="filterDiscountRangeTable()">
										30% and above
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="discountRange" value="40" v-on:change="filterDiscountRangeTable()">40% and above
<!--										<div class="common-radioIndicator"></div>-->
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="discountRange" value="50" v-on:change="filterDiscountRangeTable()">50% and above
<!--										<div class="common-radioIndicator"></div>-->
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="discountRange" value="60" v-on:change="filterDiscountRangeTable()">60% and above
<!--										<div class="common-radioIndicator"></div>-->
									</label></li>
									<li><label class="common-customRadio vertical-filters-label">
										<input type="radio" v-model="discountRange" value="0" v-on:change="filterDiscountRangeTable()">None
<!--										<div class="common-radioIndicator"></div>-->
									</label></li>
								</ul>
							</div>
						</div>
					</section>
				</div>
			</div>
			<div class="w3-col s10 m10 l10">
				<div class="w3-row">
<!--  Sliding the image-->
					<div class="w3-row">
						<div id="w3-container">
							<carousel :per-page="2" :mouse-drag="true" :autoplay="true" :autoplayTimeout="2000"
									  :loop="true">
								<slide>
									<img :src="require('@/assets/seller/seller-01.png')" alt="Chicago" width="100%"
										 height="600">
								</slide>
								<slide>
									<img :src="require('@/assets/seller/seller-25.jpg')" alt="Chicago" width="100%"
										 height="600">
								</slide>
								<slide>
									<img :src="require('@/assets/seller/seller-03.png')" alt="Chicago" width="100%"
										 height="600">
								</slide>
								<slide>
									<img :src="require('@/assets/seller/seller-26.jpg')" alt="Chicago" width="100%"
										 height="600">
								</slide>
								<slide>
									<img :src="require('@/assets/seller/seller-27.jpg')" alt="Chicago" width="100%"
										 height="600">
								</slide>
								<slide>
									<img :src="require('@/assets/seller/seller-28.jpg')" alt="Chicago" width="100%"
										 height="600">
								</slide>
							</carousel>
						</div>
					</div>
					<div class="w3-row w3-bar w3-badge w3-padding-small"> P r o d u c t</div>
					<div class="w3-row">
<!-- Showing the list of the product-->
						<div class="w3-col l6 s6 m6">
							<table class="w3-table-all w3-tiny" id="myTable"
								   style="border-left-width: 0px; padding-left: 0px; margin-top: 10px; margin-left: 5px; border-right-width: 0px; text-align: center;">
								<thead>
								<tr class="w3-light-grey w3-hover-red w3-text-green" style="font-size: 13px;">
									<td>No</td>
									<td>Category</td>
									<td>Color</td>
									<td>Discount Range</td>
									<td>Country</td>
									<td>Object</td>
									<td>Discount Range</td>
									<td>Price</td>
									<td colspan="2" class="text-center">Actions</td>
								</tr>
								</thead>
								<tbody>
								<tr class="w3-text-cyan w3-hover-blue-grey" style="font-size: 14px;"
									v-for="product in products" @click="selectProduct(product)">
									<td>
										{{product.id}}
									</td>
									<td>
										{{product.category}}
									</td>
									<td>
										{{product.color}}
									</td>
									<td>
										{{product.discountRange}}
									</td>
									<td>
										{{product.country}}
									</td>
									<td>
										{{product.object}}
									</td>
									<td>
										{{product.discountRange}} %
									</td>
									<td>
										{{product.sellPrice | currency}}
									</td>
									<td>
										<a class="w3-tooltip w3-text-yellow w3-hover-blue-grey" @click="showModal">&nbsp;
											Remove&nbsp;
											<span style="position:absolute;right:60px; width: 220px;bottom:18px;"
												  class="w3-text w3-tag">Think deeply and click!</span>
										</a>
										<modal v-show="isModalVisible" @close="closeModal"
											   v-bind:selectedProduct="selectedProduct"/>
										<a class="w3-text-red w3-hover-blue-grey"
										   v-bind:href="'/product-update/' + product.pk">&nbsp;Edit&nbsp;</a>
									</td>
								</tr>
								</tbody>
							</table>
							<div style="margin-top: 20px; text-align: center;">
                              <span class="w3-btn w3-text-blue w3-hover-red" style="padding-bottom:3px; padding-top: 3px; padding-left: 6px; paddig-right: 3px" @click="getPreviousPage()">Previous
                              </span>
                              <span class="w3-blue w3-hover-cyan" v-for="page in pages">
                                <span class="w3-btn" @click="getPage(page.link)">{{ page.pageNumber }}</span>
                              </span>
                              <span class="w3-btn w3-text-blue w3-hover-red" style="padding-bottom:3px; padding-top: 3px; padding-left: 6px; paddig-right: 3px" @click="getNextPage()">Next
                              </span>
								<router-link class="w3-btn w3-text-orange w3-hover-green" to="/">&nbsp;&nbsp;Back&nbsp;&nbsp;</router-link>
							</div><br><br>
<!--Searching objects of the table-->
							<div class="w3-row">
								<div class="w3-col m6">
									<h6 class="text-center" style="color: springgreen;">Search for a name in the table.</h6>
									<input class="w3-input w3-border w3-padding" style="margin-left: 100px; width: 200px"
										   type="text" placeholder="Search for ..." v-model="searchText" id="myInput" v-on:change="filterTable()">
								</div>
								<div class="w3-col m6">
<!--									<form action="">-->
										<h6 class="text-center" style="color: springgreen">Choose the object</h6>
										<select class="w3-hover-blue" style="margin-bottom: 60px; margin-top: 10px; margin-left: 150px;" v-model="selectedIndex" required>
											<option value="no" id="no">No</option>
											<option value="color" id="color">Color</option>
											<option value="category" id="category">Category</option>
											<option value="country" id="country">Country</option>
											<option value="object" id="object">Gender</option>
										</select>
<!--										<input type="submit">-->
<!--									</form>-->
								</div>
							</div>
                        </div>
<!-- Introducing the information of the selected product-->
						<div class="w3-col l6 s6 m6">
							<div class="card text-center" v-if="selectedProduct">{{selectedProduct.image}}
								<div>
									<div id="container">
										<carousel :per-page="1" :mouse-drag="true" :autoplay="true"
												  :autoplayTimeout="2000" :loop="true">
											<slide>
												<img :src="require('@/assets/products/show-' + (selectedProduct.id % 20).toString() + '.png')"
													 alt="Chicago" width="800" height="600">
											</slide>
										</carousel>
									</div>
									This
									<a class="w3-text-red">{{selectedProduct.category}}</a>
									made in
									<a class="w3-text-green">{{selectedProduct.factory}}</a>
									company of
									<a class="w3-text-yellow">{{selectedProduct.country}}.</a>
								</div>
								<div class="card-block">
									<p class="card-text"></p>
									<p class="card-text">The buyprice is <a class="w3-text-red">{{selectedProduct.buyPrice}}$</a>.
									</p>
									<p class="card-text">And this recieved the evaluation of
										"{{selectedProduct.description}}" and {{selectedProduct.review}} review from
										clients.</p>
									<a class="w3-text-yellow w3-hover-red"
									   v-bind:href="'/product-update/' + selectedProduct.id">Edit</a>
									<a class="w3-tooltip w3-text-yellow w3-hover-red" @click="showModal" target="_top">
										Remove
										<span style="position:absolute;left:50px; width: 240px;bottom:22px;"
											  class="w3-text w3-tag">Don't press without thinking!</span>
									</a>
									<modal v-show="isModalVisible" @close="closeModal"
										   v-bind:selectedProduct="selectedProduct"/>
								</div>
							</div>
							<div class="w3-hover-blue" v-else="!selectedProduct">
								<img :src="require('@/assets/seller/seller-0.png')" alt="Showing" width="800" height="600">
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
<!-- Showing the image of product -->
		<div class="w3-row">
			<div class="w3-container">
				<span class="w3-col m1">
					<img :src="require('@/assets/products/show-1.png')" style="width:70%; heigt:70%; cursor:zoom-in"
						 onclick="document.getElementById('modal01').style.display='block'">
					<div id="modal01" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-1.png')" style="width:100%">
						</div>
					</div>
				</span>
				<span class="w3-col m1">
					<img :src="require('@/assets/products/show-2.png')" style="width:100%; heigt:100%; cursor:zoom-in"
						 onclick="document.getElementById('modal02').style.display='block'">
					<div id="modal02" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-2.png')" style="width:100%">
						</div>
					</div>
				</span>
				<span class="w3-col m1">
					<img :src="require('@/assets/products/show-3.png')" style="width:100%; heigt:100%; cursor:zoom-in"
						 onclick="document.getElementById('modal03').style.display='block'">
					<div id="modal03" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-3.png')" style="width:100%">
						</div>
					</div>
				</span>
				<span class="w3-col m1">
						<img :src="require('@/assets/products/show-7.png')" style="width:100%; heigt:100%; cursor:zoom-in"
							 onclick="document.getElementById('modal07').style.display='block'">
					<div id="modal07" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-7.png')" style="width:100%">
						</div>
					</div>
				</span>
				<span class="w3-col m1">
						<img :src="require('@/assets/products/show-8.png')" style="width:100%; heigt:100%; cursor:zoom-in"
							 onclick="document.getElementById('modal08').style.display='block'">
						<div id="modal08" class="w3-modal" onclick="this.style.display='none'">
							<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
							<div class="w3-modal-content w3-animate-zoom">
								<img :src="require('@/assets/products/show-8.png')" style="width:100%">
							</div>
						</div>
				</span>
				<span class="w3-col m1">
					<img :src="require('@/assets/products/show-6.png')" style="width:100%; heigt:100%; cursor:zoom-in"
						 onclick="document.getElementById('modal06').style.display='block'">
					<div id="modal06" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-6.png')" style="width:100%">
						</div>
					</div>
				</span>
				<span class="w3-col m1">
					<img :src="require('@/assets/products/show-14.png')" style="width:100%; heigt:100%; cursor:zoom-in"
						 onclick="document.getElementById('modal04').style.display='block'">
					<div id="modal04" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-14.png')" style="width:100%">
						</div>
					</div>
				</span>

				<span class="w3-col m1">
					<img :src="require('@/assets/products/show-15.png')" style="width:100%; heigt:100%; cursor:zoom-in"
						 onclick="document.getElementById('modal5').style.display='block'">
					<div id="modal5" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-15.png')" style="width:100%">
						</div>
					</div>
				</span>

				<span class="w3-col m1">
					<img :src="require('@/assets/products/show-9.png')" style="width:100%; heigt:100%; cursor:zoom-in"
						 onclick="document.getElementById('modal09').style.display='block'">
					<div id="modal09" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-9.png')" style="width:100%">
						</div>
					</div>
				</span>
				<span class="w3-col m1">
					<img :src="require('@/assets/products/show-10.png')" style="width:100%; heigt:100%; cursor:zoom-in"
						 onclick="document.getElementById('modal10').style.display='block'">
					<div id="modal10" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-10.png')" style="width:100%">
						</div>
					</div>
				</span>
				<span class="w3-col m1">
					<img :src="require('@/assets/products/show-11.png')" style="width:100%; heigt:100%; cursor:zoom-in"
						 onclick="document.getElementById('modal11').style.display='block'">
					<div id="modal11" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-11.png')" style="width:100%">
						</div>
					</div>
				</span>
				<span class="w3-col m1">
					<img :src="require('@/assets/products/show-12.png')" style="width:100%; heigt:100%; cursor:zoom-in"
						 onclick="document.getElementById('modal12').style.display='block'">
					<div id="modal12" class="w3-modal" onclick="this.style.display='none'">
						<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
						<div class="w3-modal-content w3-animate-zoom">
							<img :src="require('@/assets/products/show-12.png')" style="width:100%">
						</div>
					</div>
				</span>
			</div>
		</div>
	</div>
</template>
<script>
	/* eslint-disable */
	import {APIService} from '../http/APIService'
	import Loading from './Loading'

	import HistoricalRecord from './SellerComponents/HistoricalRecord'
	import ProductDescription from './SellerComponents/ProductDescription'
	import SellersList from './SellerComponents/SellersList'
	import DeliveryState from './SellerComponents/DeliveryState'
	import Modal from './Modal.vue'

	const API_URL = 'http://localhost:8000'
	const apiService = new APIService()

	export default {
		name: 'ProductList',
		components: {
			Loading,
			HistoricalRecord,
			ProductDescription,
			SellersList,
			DeliveryState,
			Modal
		},
		data() {
			return {
				selectedProduct: null,
				products: [],
				searchText: '',
				numberOfPages: 0,
				pages: [],
				numberOfProducts: 0,
				loading: false,
				nextPageURL: '',
				previousPageURL: '',
				selectedIndex: -1,
				isModalVisible: false,
				price: -1,
				discountRange: -1,
				colorRed: -1,
				colorGreen: -1,
				colorBlack: -1,
				colorBlue: -1,
				colorYellow: -1,
				categoryTshirts: -1,
				categoryShoes: -1,
				categoryJeans: -1,
				categoryTrousers: -1,
				categoryJackets: -1,
				categorySportsShoes: -1,
				genderMale: -1,
				genderFemale: -1,
				genderBoy: -1,
				genderGirl: -1
			}
		},
		// watch: {
		// 	price: function () {
		// 		this.filterPriceTable()
		// 	}
		// },
		methods: {
			filterTable() {
				if (this.searchText === '') return
				if(this.selectedIndex == 'no') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].no != this.searchText)
							this.products.splice(i, 1)
					}
				}
				else if(this.selectedIndex == 'category') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].category != this.searchText)
							this.products.splice(i, 1)
					}
				}
				else if(this.selectedIndex == 'object') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].object != this.searchText)
							this.products.splice(i, 1)
					}
				}
				else if(this.selectedIndex == 'country') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].country != this.searchText)
							this.products.splice(i, 1)
					}
				}
				else if(this.selectedIndex == 'color') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].color != this.searchText)
							this.products.splice(i, 1)
					}
				}
			},
			filterPriceTable() {
				// if (this.price.toString() === -1) return
				if(this.price.toString() == '50') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].sellPrice >= 50)
							this.products.splice(i, 1)
					}
				}
				else if (this.price.toString() == '100') {

					for (var i = this.products.length - 1; i >= 0; i--) {
						if ((this.products[i].sellPrice < 50) || ((this.products[i].sellPrice >= 100)))
							this.products.splice(i, 1)
					}
				}

				else if (this.price.toString() == '500') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if ((this.products[i].sellPrice < 100) || (this.products[i].sellPrice >= 500))
							this.products.splice(i, 1)
					}
				}

				else if (this.price.toString() == '2000') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if ((this.products[i].sellPrice < 500) || (this.products[i].sellPrice >= 2000))
							this.products.splice(i, 1)
					}
				}

				else if(this.price.toString() == '2001') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].sellPrice <= 2000)
							this.products.splice(i, 1)
					}
				}
				else
					this.price = -1
			},
			filterDiscountRangeTable() {
				if(this.discountRange.toString() == '10') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].discountRange < 10)
							this.products.splice(i, 1)
					}
				}
				else if (this.discountRange.toString() == '20') {

					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].discountRange < 20)
							this.products.splice(i, 1)
					}
				}

				else if (this.discountRange.toString() == '30') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].discountRange < 30)
							this.products.splice(i, 1)
					}
				}

				else if (this.discountRange.toString() == '40') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].discountRange < 40)
							this.products.splice(i, 1)
					}
				}

				else if(this.discountRange.toString() == '50') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].discountRange < 50)
							this.products.splice(i, 1)
					}
				}
				else if(this.discountRange.toString() == '60') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].discountRange < 60)
							this.products.splice(i, 1)
					}
				}
				else
					this.discountRange = -1
					for (var i = this.products.length - 1; i >= 0; i--) {
						return
					}
			},
			filterColorTable() {
				//alert(this.colorYellow)
				// if (this.price.toString() === -1) return
				if(this.colorRed.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].color == 'red')
							this.products.splice(i, 1)
					}
				}
				else
					this.colorRed = -1
				if(this.colorGreen.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].color == 'green')
							this.products.splice(i, 1)
					}
				}
				else
					this.colorGreen = -1
				if(this.colorBlack.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].color == 'black')
							this.products.splice(i, 1)
					}
				}
				else
					this.colorBlack = -1
				if(this.colorBlue.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].color == 'blue')
							this.products.splice(i, 1)
					}
				}
				else
					this.colorBlue = -1
				if(this.colorYellow.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].color == 'yellow')
							this.products.splice(i, 1)
					}
				}
				else
					this.colorYellow = -1
			},
			filterCategoryTable() {
				if(this.categoryTshirts.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].category == 'Tshirts')
							this.products.splice(i, 1)
					}
				}
				else
					this.categoryTshirts = -1
				if(this.categoryShoes.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].category == 'Shoes')
							this.products.splice(i, 1)
					}
				}
				else
					this.categoryShoes = -1
				if(this.categoryJeans.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].category == 'Jeans')
							this.products.splice(i, 1)
					}
				}
				else
					this.categoryJeans = -1
				if(this.categoryTrousers.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].category == 'Trousers')
							this.products.splice(i, 1)
					}
				}
				else
					this.categoryTrousers = -1
				if(this.categoryJackets.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].category == 'Jackets')
							this.products.splice(i, 1)
					}
				}
				else
					this.categoryJackets = -1
				if(this.categorySportsShoes.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].category == 'SportsShoes')
							this.products.splice(i, 1)
					}
				}
				else
					this.categorySportsShoes = -1
			},
			filterGenderTable() {
				if(this.genderMale.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].object == 'male')
							this.products.splice(i, 1)
					}
				}
				else
					this.genderMale = -1
				if(this.genderFemale.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].object == 'female')
							this.products.splice(i, 1)
					}
				}
				else
					this.genderFemale = -1
				if(this.genderBoy.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].object == 'boy')
							this.products.splice(i, 1)
					}
				}
				else
					this.genderBoy = -1
				if(this.genderGirl.toString() == 'false') {
					for (var i = this.products.length - 1; i >= 0; i--) {
						if (this.products[i].object == 'girl')
							this.products.splice(i, 1)
					}
				}
				else
					this.genderGirl = -1
			},
			showModal() {
				this.isModalVisible = true
			},
			closeModal() {
				this.isModalVisible = false
			},
			getProducts() {

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
			}
			,
			getPage(link) {
				this.loading = true
				apiService.getProductsByURL(link).then((page) => {
					this.products = page.data
					this.nextPageURL = page.nextlink
					this.previousPageURL = page.prevlink
					this.loading = false
					this.filterTable()
					this.filterPriceTable()
					this.filterDiscountRangeTable()
					this.filterColorTable()
					this.filterCategoryTable()
					this.filterGenderTable()
				})
			}
			,
			getNextPage() {
				this.loading = true
				apiService.getProductsByURL(this.nextPageURL).then((page) => {
					this.products = page.data
					this.nextPageURL = page.nextlink
					this.previousPageURL = page.prevlink
					this.loading = false
				})

			}
			,
			getPreviousPage() {
				this.loading = true
				apiService.getProductsByURL(this.previousPageURL).then((page) => {
					this.products = page.data
					this.nextPageURL = page.nextlink
					this.previousPageURL = page.prevlink
					this.loading = false
				})

			}
			,
			deleteProduct(product) {
				apiService.deleteProduct(product).then((r) => {
					if (r.status === 204) {
						/*for(var i = this.products.length-1; i--;){
							console.log(this.products[i].pk);
							if (this.products[i].pk === product.pk)
							{
							  console.log("deleting product " + this.products[i].pk)
							  this.products.splice(i, 1);
							}
						  }*/
						this.$router.go()

					}
				})
			}
			,
			selectProduct(product) {
				this.selectedProduct = product
			}
		},

		mounted() {
			this.getProducts()
		}
	}
</script>

<style scoped>
</style>
