
/* eslint-disable */

import Vue from 'vue'
import Router from 'vue-router'
import ProductList from '@/components/ProductList'
import ProductCreate from '@/components/ProductCreate'
import Callback from '@/components/Callback'
import Home from '@/components/Home'
import AuthService from '../auth/AuthService'
import HistoricalRecord from '../components/SellerComponents/HistoricalRecord'
import ProductDescription from '../components/SellerComponents/ProductDescription'
import SellersList from '../components/SellerComponents/SellersList'
import DeliveryState from '../components/SellerComponents/DeliveryState'
import ProductOptions from '../components/ProductComponents/ProductOptions'

Vue.use(Router)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/product-list',
    name: 'ProductList',
    component: ProductList,
    meta: { requiresAuth : true }
  },
  {
    path: '/product-create',
    name: 'ProductCreate',
    component: ProductCreate,
    meta: { requiresAuth : true }
  },
  {
    path: '/product-update/:pk',
    name: 'ProductUpdate',
    component: ProductCreate
  },
  {
    path: '/callback',
    name: 'Callback',
    component: Callback
  },
  {
    path: '/Historical-Record',
    name: 'HistoricalRecord',
    component: HistoricalRecord
  },
  {
    path: '/Product-Description',
    name: 'ProductDescription',
    component: ProductDescription
  },
  {
    path: '/Sellers-List',
    name: 'SellersList',
    component: SellersList
  },
  {
    path: '/Delivery-State',
    name: 'DeliveryState',
    component: DeliveryState
  },
  {
    path: '/Product-Options',
    name: 'ProductOptions',
    component: ProductOptions
  },

  ]

const router = new Router({
  mode: 'history',
  routes
})

//const auth = new AuthService()

router.beforeEach((to, from, next) => {
  if(to.meta.requiresAuth)
  {
    if(!AuthService.authenticated())
    {
      next('/');
    }
  }
  next()
})

export function authGuard(to, from, next) {

  if(!AuthService.authenticated()){
    next('/');
  }
  next()

}

export default router
