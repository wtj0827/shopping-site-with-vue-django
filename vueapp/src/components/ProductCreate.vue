<template>

	<div id="container" class="container">
      <div class="w3-container w3-hover-cyan w3-yellow w3-center" style="margin-top: 50px"><h1>Create a Product</h1></div>
		<div class="row" style="margin-top: 50px">
			<div class="w3-col m4">
				<img src="../assets/seller/seller-21.jpg" class="w3-circle" alt="Lights" style="margin-left: 40px; width:70%"><br><br>
				<img src="../assets/seller/seller-22.jpg" class="w3-circle" alt="Lights" style="margin-left: 40px; width:70%">
				<br><br><br><br>
				<div class="w3-container w3-teal">
					<h1 style="text-align: center">Summer 2019</h1>
				</div>
				<div class="w3-row-padding w3-margin-top">
					<div class="w3-third">
						<div class="w3-card">
							<img :src="require('@/assets/seller/seller-21.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
								 onclick="document.getElementById('modal01').style.display='block'">
							<div id="modal01" class="w3-modal" onclick="this.style.display='none'">
								<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
								<div class="w3-modal-content w3-animate-zoom">
									<img :src="require('@/assets/seller/seller-21.jpg')" style="width:100%">
								</div>
							</div>
							<div class="w3-container">
								<h5>5 Terre</h5>
							</div>
						</div>
					</div>
					<div class="w3-third">
						<div class="w3-card">
							<img :src="require('@/assets/seller/seller-22.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
								 onclick="document.getElementById('modal02').style.display='block'">
							<div id="modal02" class="w3-modal" onclick="this.style.display='none'">
								<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
								<div class="w3-modal-content w3-animate-zoom">
									<img :src="require('@/assets/seller/seller-22.jpg')" style="width:100%">
								</div>
							</div>
							<div class="w3-container">
								<h5>Monterosso</h5>
							</div>
						</div>
					</div>
					<div class="w3-third">
						<div class="w3-card">
							<img :src="require('@/assets/seller/seller-27.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
								 onclick="document.getElementById('modal03').style.display='block'">
							<div id="modal03" class="w3-modal" onclick="this.style.display='none'">
								<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
								<div class="w3-modal-content w3-animate-zoom">
									<img :src="require('@/assets/seller/seller-27.jpg')" style="width:100%">
								</div>
							</div>
							<div class="w3-container">
								<h5>Vernazza</h5>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="w3-col m4 col-sm-3">
				<div>
					<h1 class="w3-text-red" style="text-align: center;">Add the detail of the production to Database<br><br></h1>
				</div>
				<div class="alert alert-warning" v-show="showCreateMessage">
					<button type="button" class="close" @click="hideMessage()">X</button>
					<strong>Product successfully created!</strong>
				</div>
				<div class="alert alert-warning" v-show="showUpdateMessage">
					<button type="button" class="close" @click="hideMessage()">X</button>
					<strong>Product successfully updated!</strong>
				</div>

				<div class="alert alert-warning" v-show="showError">
					<button type="button" class="close" @click="hideMessage()">X</button>
					<strong>Error!</strong>
				</div>

				<div class="info-form w3-display-container">
					<form class="w3-card">
						<div class="form-group w3-text-cyan">
							<label for="sku">Product sku</label>
							<input v-model="product.sku" type="text" class="form-control w3-hover-cyan" id="sku"
								   aria-describedby="skuHelp"
								   placeholder="Enter SKU">
						    <label for="category">Product category</label>
						    <input v-model="product.category" type="text" class="form-control" id="category"
								 aria-describedby="categoryHelp" placeholder="Enter category">
						    <small id="categoryHelp" class="form-text text-muted">Enter your product's category</small>

							<label for="country">Product country</label>
							<input v-model="product.country" type="text" class="form-control w3-hover-cyan" id="country"
								   aria-describedby="countryHelp" placeholder="Enter country">
							              <label for="image">Product image</label>
							              <input v-model="product.image" type="text" class="form-control" id="image" aria-describedby="imageHelp"
							                     placeholder="Enter image">
							              <small id="imageHelp" class="form-text text-muted">Enter your product's image</small>
							<label for="description">Product Description</label>
							<textarea v-model="product.description" class="form-control w3-hover-cyan" id="description" aria-describedby="descHelp" placeholder="Enter description"></textarea>
							<label for="review">Product review</label>
							<textarea v-model="product.review" class="form-control w3-hover-cyan" id="review" aria-describedby="reviewHelp" placeholder="Enter review"></textarea>

							<label for="object">Product object</label>
							<input v-model="product.object" type="text" class="form-control w3-hover-cyan" id="object"
								   aria-describedby="objectHelp"
								   placeholder="Enter object">
							<label for="buyPrice">Product buyPrice</label>
							<input v-model="product.buyPrice" type="text" class="form-control w3-hover-cyan" id="buyPrice"
								   aria-describedby="buyPriceHelp" placeholder="Enter the buyPrice">
							<label for="sellPrice">Product sellPrice</label>
							<input v-model="product.sellPrice" type="text" class="form-control w3-hover-cyan" id="sellPrice"
								   aria-describedby="sellPriceHelp" placeholder="Enter sellPrice">
							<label for="unit">Product unit</label>
							<input v-model="product.unit" type="text" class="form-control w3-hover-cyan" id="unit"
								   aria-describedby="unitHelp"
								   placeholder="Enter unit">
							<label for="quantity">Product quantity</label>
							<input v-model="product.quantity" type="text" class="form-control w3-hover-cyan" id="quantity"
								   aria-describedby="quantityHelp" placeholder="Enter quantity">
						</div>
					</form>
					<!-- Start modifying: KYG_2019/12/25-->
					<div class="text-center">
						<button class="btn btn-primary w3-blue w3-padding w3-hover-red" v-if="!this.product.pk" @click="createProduct()">
							<span v-if="!creating">Create</span>
							<span v-if="creating">Creating... Please wait </span>
						</button>
						<button class="btn btn-primary w3-blue w3-padding w3-hover-red" v-if="this.product.pk" @click="updateProduct()">
							<span v-if="!updating">Update</span>
							<span v-if="updating">Updating... Please wait </span>
						</button>
						<button class="btn btn-primary w3-blue w3-padding w3-hover-red" @click="newProduct()">New..</button>
						<router-link to="/product-list" class="btn w3-blue w3-padding w3-hover-red">
							Back
						</router-link>
					</div>
				</div>
			</div>

			<div class="w3-col m4">
				<img src="../assets/seller/seller-26.jpg" class="w3-circle w3-animate-zoom" alt="Lights" style="margin-left: 40px; width:70%"><br><br>
				<img src="../assets/seller/seller-27.jpg" class="w3-circle w3-animate-zoom" alt="Lights" style="margin-left: 40px; width:70%">
				<br><br><br>
				<div class="w3-container w3-teal">
					<h1 style="text-align: center">Summer 2019</h1>
				</div>

				<div class="w3-row-padding w3-margin-top">
					<div class="w3-third">
						<div class="w3-card w3-animate-zoom">
							<img :src="require('@/assets/seller/seller-24.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
								 onclick="document.getElementById('modal04').style.display='block'">
							<div id="modal04" class="w3-modal" onclick="this.style.display='none'">
								<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
								<div class="w3-modal-content w3-animate-zoom">
									<img :src="require('@/assets/seller/seller-24.jpg')" style="width:100%">
								</div>
							</div>
							<div class="w3-container">
								<h5>Manarola</h5>
							</div>
						</div>
					</div>

					<div class="w3-third">
						<div class="w3-card">
							<img :src="require('@/assets/seller/seller-25.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
								 onclick="document.getElementById('modal05').style.display='block'">
							<div id="modal05" class="w3-modal" onclick="this.style.display='none'">
								<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
								<div class="w3-modal-content w3-animate-zoom">
									<img :src="require('@/assets/seller/seller-25.jpg')" style="width:100%">
								</div>
							</div>
							<div class="w3-container">
								<h5>Corniglia</h5>
							</div>
						</div>
					</div>

					<div class="w3-third">
						<div class="w3-card">
							<img :src="require('@/assets/seller/seller-26.jpg')" style="width:100%; heigt:100%; cursor:zoom-in"
								 onclick="document.getElementById('modal06').style.display='block'">
							<div id="modal06" class="w3-modal" onclick="this.style.display='none'">
								<span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
								<div class="w3-modal-content w3-animate-zoom">
									<img :src="require('@/assets/seller/seller-26.jpg')" style="width:100%">
								</div>
							</div>
							<div class="w3-container">
								<h5>Riomaggiore</h5>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

</template>

<script>
	/* eslint-disable */
	function sleep(time) {
		return new Promise((resolve) => setTimeout(resolve, time))
	}

	import {APIService} from '../http/APIService'

	const apiService = new APIService()

	export default {
		name: 'ProductCreate',
		components: {},
		data() {
			return {
				showCreateMessage: false,
				showUpdateMessage: false,
				showError: false,
				product: {},
				products: '',
				creating: false,
				updating: false
			}
		},
		methods: {
			hideMessage() {
				this.showCreateMessage = false
				this.showUpdateMessage = false
				this.showError = false
			},
			createProduct() {
				this.creating = true
				apiService.createProduct(this.product).then((result) => {
					// success
					if (result.status === 201) {
						this.product = result.data
						this.showCreateMessage = true

					}
					sleep(1000).then(() => {
						this.creating = false
					})
				}, (error) => {
					this.showError = true
					sleep(1000).then(() => {
						this.creating = false
					})
				})
			},
			updateProduct() {
				this.updating = true
				apiService.updateProduct(this.product).then((result) => {
					// success
					if (result.status === 200) {
						//this.product = {};
						this.showUpdateMessage = true

						sleep(1000).then(() => {
							this.updating = false
						})

					}
				}, (error) => {
					this.showError = true
					sleep(1000).then(() => {
						this.updating = false
					})
				})
			},
			newProduct() {
				this.product = {}
			}

		},
		mounted() {

			if (this.$route.params.pk) {
				apiService.getProduct(this.$route.params.pk).then((product) => {
					this.product = product
					console.log(this.product.name)
				})
			}
		},
	}
</script>
<style scoped>
	.aform {
		margin-left: auto;
		width: 60%;
	}
</style>
