<template>
	<div class="w3-container w3-hover-cyan">
		<section>
			<div class="condition-render-verticalFilters condition-render-boundary-top" style="top: 0px; bottom: auto;">
				<div class="vertical-filters-filters header-container">
          <span class="header-title mdl-color-text--blue-400">
            <br>
             <h6 class="d-print-inline text-secondary text-md-center">Select the attributes of the product <br>you want to buy</h6>
            <br>
          </span>
				</div>
				<div class="vertical-filters-filters header-container">
          <span class="header-title mdl-color-text--blue-400">
            <h6 class="table-hover">Object</h6></span>
				</div>

				<div class="vertical-filters-filters">
					<ul class="gender-list">
						<li><label class="common-customRadio gender-label undefined"><input type="radio" value="men">
							Men</label></li>
						<li><label class="common-customRadio gender-label"><input type="radio" form="myform" value="women">
							women</label></li>
						<li><label class="common-customRadio gender-label"><input type="radio" form="myform" value="boys">
							Boys</label></li>
						<li><label class="common-customRadio gender-label"><input type="radio" form="myform" value="girls">
							Girls</label></li>
						<li><label class="common-customRadio gender-label"><input type="radio" form="myform" value="unknown" checked>
							Unknown</label></li>
					</ul>
				</div>

				<div class="vertical-filters-filters categories-container ">
          <span class="vertical-filters-header mdl-color-text--blue-400"><h6
				  class="table-hover">Categories</h6></span>
					<div class="filter-search-filterSearchBox">
						<input type="text" class="text-center filter-search-inputBox filter-search-hidden bg-warning"
							   placeholder="Search for Categories">
						<span class="myntraweb-sprite filter-search-iconSearch sprites-search"></span>
					</div>
					<ul class="categories-list">
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Tshirts">
							Tshirts
						</label></li>
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Casual Shoes">
							Shoes
						</label></li>
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Jeans">
							Jeans
						</label></li>
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Trousers">
							Trousers
						</label></li>
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Trousers">
							Jackets
						</label></li>
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Sports Shoes">
							Sports Shoes
						</label></li>
					</ul>
				</div>

				<div class="vertical-filters-filters categories-container">
					<span class="vertical-filters-header mdl-color-text--blue-400"><h6 class="table-hover">Color</h6></span>
					<div class="filter-search-filterSearchBox">
						<input type="text" class="text-center filter-search-inputBox filter-search-hidden bg-warning"
							   placeholder="Search for Color">
						<span class="myntraweb-sprite filter-search-iconSearch sprites-search"></span>
					</div>
					<ul class="categories-list">
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Tshirts">
							Red
						</label></li>
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Casual Shoes">
							Green
						</label></li>
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Jeans">
							Black
						</label></li>
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Trousers">
							Blue
						</label></li>
						<li><label class="common-customCheckbox vertical-filters-label"><input type="checkbox"
																							   value="Trousers">
							Yellow
						</label></li>
					</ul>
				</div>

				<div class="vertical-filters-filters">
					<span class="vertical-filters-header mdl-color-text--blue-400"><h6 class="table-hover">Price</h6></span>
					<ul class="price-list">
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="price" name="price" value="50$ or less">50$ or less
						</label></li>
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="price" name="price" value="51$ to 100$">51$ to 100$
						</label></li>
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="price" name="price" value="101$ to 500$">101$ to 500$
						</label></li>
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="price" name="price" value="501$ to 2000$">501$ to 2000$
						</label></li>
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="price" name="price" value="2001$ or more">2001$ or more
						</label></li>
					</ul>
				</div>

				<div class="vertical-filters-filters"><span class="vertical-filters-header mdl-color-text--blue-400">
          <h6 class="table-hover">Payment method</h6></span>
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


				<div class="vertical-filters-filters"><span class="vertical-filters-header mdl-color-text--blue-400">
          <h6 class="table-hover">Discount Range</h6></span>
					<ul class="discount-list">
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="discount-input" name="discount-product" value="10.0 TO 100.0">
							10% and
							above
						</label></li>
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="discount-input" name="discount-product" value="20.0 TO 100.0">20%
							and above
							<div class="common-radioIndicator"></div>
						</label></li>
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="discount-input" name="discount-product" value="30.0 TO 100.0">
							30% and
							above
						</label></li>
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="discount-input" name="discount-product" value="40.0 TO 100.0">40%
							and above
							<div class="common-radioIndicator"></div>
						</label></li>
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="discount-input" name="discount-product" value="50.0 TO 100.0">50%
							and above
							<div class="common-radioIndicator"></div>
						</label></li>
						<li><label class="common-customRadio vertical-filters-label">
							<input type="radio" class="discount-input" name="discount-product" value="60.0 TO 100.0">60%
							and above
							<div class="common-radioIndicator"></div>
						</label></li>
					</ul>
				</div>
			</div>
		</section>
	</div>
</template>

<script>
  export default {
    name: 'ProductOptions'
  }
</script>

<style scoped>

</style>
