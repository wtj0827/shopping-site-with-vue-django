import {APIService} from '../http/APIService'
// import ProductOptions from './ProductComponents/ProductOptions'
 const API_URL = 'http://localhost:8000'
const apiService = new APIService()

export default {
  name: 'PageManagement',
  data () {
    return {
      selectedProduct: null,
      products: [],
      numberOfPages: 0,
      pages: [],
      numberOfProducts: 0,
      loading: false,
      nextPageURL: '',
      previousPageURL: '',
      selectedIndex: -1,
      isModalVisible: false
      // imgNum: ''
    }
  },
  methods: {
    // showModal () {
    //   this.isModalVisible = true
    // },
    // closeModal () {
    //   this.isModalVisible = false
    // },
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
    }
    ,
    getPage (link) {
      this.loading = true
      apiService.getProductsByURL(link).then((page) => {
        this.products = page.data
        this.nextPageURL = page.nextlink
        this.previousPageURL = page.prevlink
        this.loading = false
      })
    }
    ,
    getNextPage () {
      this.loading = true
      apiService.getProductsByURL(this.nextPageURL).then((page) => {
        this.products = page.data
        this.nextPageURL = page.nextlink
        this.previousPageURL = page.prevlink
        this.loading = false
      })
    }
    ,
    getPreviousPage () {
      this.loading = true
      apiService.getProductsByURL(this.previousPageURL).then((page) => {
        this.products = page.data
        this.nextPageURL = page.nextlink
        this.previousPageURL = page.prevlink
        this.loading = false
      })
    },
    deleteProduct (product) {
      apiService.deleteProduct(product).then((r) => {
        if (r.status === 204) {
          this.$router.go()
        }
      })
    },
    selectProduct (product) {
      this.selectedProduct = product
    }
  }
  ,
  mounted () {
    this.getProducts()
  }
}
