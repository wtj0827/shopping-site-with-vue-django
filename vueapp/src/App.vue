<template>
  <div id="main">
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark" id="nav">
      <div><span>Free shipping  for standard order over $100</span></div>
      <div id="navbar-menu">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a href="/">Home</a>
          </li>
          <!--          <li class="nav-item">-->
          <!--            <a href="/product-list">Products</a>-->
          <!--          </li>-->
          <!-- modifying: KYG_2019/12/25-->
          <li class="nav-item">
            <a href="/product-list">Seller</a>
          </li>
          <li class="nav-item">
            <a href="/product-create">Create</a>
          </li>
          <li class="nav-item" v-if="!authenticated" @click="login()">
            <a>Login</a>
          </li>
          <li class="nav-item" v-if="authenticated" @click="logout()">
            <a>Logout</a>
          </li>
        </ul>
      </div>
    </nav>

    <div class="container">
      <router-view
        :auth="auth"
        :authenticated="authenticated">
      </router-view>
    </div>

    <footer class="container-fluid footer text-left mt-3">
      <div class="container">
        <div class="row" style="padding-bottom: 30px">
          <div class="col-sm-6 col-lg-3 p-b-50">
            <h4 class="stext-301 cl0 p-b-30">
              Categories
            </h4>

            <ul>
              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Women
                </a>
              </li>

              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Men
                </a>
              </li>

              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Shoes
                </a>
              </li>

              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Watches
                </a>
              </li>
            </ul>
          </div>
          <div class="col-sm-6 col-lg-3 p-b-50">
            <h4 class="stext-301 cl0 p-b-30">
              Categories
            </h4>

            <ul>
              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Women
                </a>
              </li>

              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Men
                </a>
              </li>

              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Shoes
                </a>
              </li>

              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Watches
                </a>
              </li>
            </ul>
          </div>
          <div class="col-sm-6 col-lg-3 p-b-50">
            <h4 class="stext-301 cl0 p-b-30">
              Categories
            </h4>

            <ul>
              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Women
                </a>
              </li>

              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Men
                </a>
              </li>

              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Shoes
                </a>
              </li>

              <li class="p-b-10">
                <a href="#" class="stext-107 cl7 hov-cl1 trans-04">
                  Watches
                </a>
              </li>
            </ul>
          </div>
          <div class="col-sm-6 col-lg-3 p-b-50">
            <h4>
              Newsletter
            </h4>

            <form>
              <div class="form-group">
                <input class="form-control" type="email" name="email" placeholder="email@example.com">
                <div class="focus-input1 trans-04"></div>
              </div>

              <div class="p-t-17">
                <button class="btn btn-secondary">
                  Subscribe
                </button>
              </div>
            </form>
          </div>
        </div>
        <div class="p-t-40" id="footer-link">
          <div class="flex-c-m flex-w p-b-18" id="footer-link-items">
            <a href="#" class="m-all-1">
              <img src="./assets/icons/icon-pay-01.png" alt="ICON-PAY">
            </a>

            <a href="#" class="m-all-1">
              <img src="./assets/icons/icon-pay-02.png" alt="ICON-PAY">
            </a>

            <a href="#" class="m-all-1">
              <img src="./assets/icons/icon-pay-03.png" alt="ICON-PAY">
            </a>

            <a href="#" class="m-all-1">
              <img src="./assets/icons/icon-pay-04.png" alt="ICON-PAY">
            </a>

            <a href="#" class="m-all-1">
              <img src="./assets/icons/icon-pay-05.png" alt="ICON-PAY">
            </a>
          </div>
          <p class="<">
            <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
            Copyright ©2019 All rights reserved | This site is made with <i class="fa fa-heart-o"
                                                                            aria-hidden="true"></i> by <a
            href="https://colorlib.com" target="_blank">Aurora</a>
            <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->

          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
  /* eslint-disable */
  import AuthService from './auth/AuthService'

  const auth = new AuthService()
  const {login, logout, authenticated, authNotifier} = auth

  export default {
    name: 'app',
    data () {
      authNotifier.on('authChange', authState => {
        this.authenticated = authState.authenticated
      })
      return {
        auth,
        authenticated
      }
    },
    methods: {
      login,
      logout
    }
  }
</script>

<style>
  @import "../node_modules/bootstrap/dist/css/bootstrap.min.css";

  html {
    min-height: 100%;
  }

  body {
    min-height: 100%;
  }

  #main {
    position: relative;
    min-height: 100%;
  }

  #nav {
    background-color: #222 !important;
    font-size: 14px;
    color: #b2b2b2;
    height: 40px;
    padding: 0px 100px;
    min-width: 1100px;
  }

  #navbar-menu {
    position: absolute;
    right: 0px;
    margin-right: 30px;
  }

  .nav-item {
    margin-left: 5px;
    background-color: transparent;
    margin: 0px;
  }

  .nav-item a {
    text-decoration: none;
    color: #b2b2b2;
    padding: 0px 5px;
  }

  .nav-item a:hover {
    color: white;
  }

  .container {
    margin: 0px;
    padding: 0px;
    width: 100%;
    max-width: 100%;
  }

  .footer {
    position: relative;
    bottom: 0px;
    width: 100%;
    background-color: #222;
    padding: 30px 50px 10px 50px;
    margin-top: 300px;
  }

  .footer p {
    color: white;
  }

  .footer h4 {
    color: #e4dede;
    font-size: 16px;
    font-family: Montserrat-Bold;
    text-transform: uppercase;
    line-height: 1.6;
    padding-bottom: 20px;
  }

  .footer ul {
    padding: 0px;

    list-style-type: none;
  }

  .footer ul a {
    color: #b2b2b2;
    font-size: 14px;
  }

  .footer ul a:hover {
    text-decoration: none;
    color: blueviolet;
  }

  #footer-link-items {
    text-align: center;
  }

  #footer-link p {
    text-align: center;
    color: grey;
    padding-top: 20px;
  }

</style>
