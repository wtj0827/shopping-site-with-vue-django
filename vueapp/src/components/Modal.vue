<template>
  <!-- // <transition name="message">-->
  <transition name="modal">

      <div class="modal modal-container">
        <section class="modal-body">
          <slot name="body">
            Do you delete the data really?
          </slot>
        </section>
        <footer class="modal-footer">
          <slot name="footer">
            <button type="button " class="btn-green btn-toolbar" @click="close">
              Cancel
            </button>
            <button type="button" class="btn-green align-content" @click="deleteProduct(selectedProduct)">
              Ok
            </button>
          </slot>
        </footer>
      </div>

  </transition>
</template>

<script>
  import {APIService} from '../http/APIService'

  const apiService = new APIService()
  export default {
    name: 'modal',
    data () {
      return {
        selectedProduct: null,
        products: []
      }
    },
    props: {
      selectedProduct: Number
    },
    methods: {
      close () {
        this.$emit('close')
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
  }
</script>

<style scoped>
  .modal-fade-enter,
  .modal-fade-leave-active {
    opacity: 0;
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity .5s ease
  }

  .modal-container {
    width: 300px;
    max-width: 80%;
    height: 200px;
    max-height: 80%;
    margin: 0px auto;
    margin-left: 600px;
    margin-top: 200px;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
    transition: all .3s ease;
    font-family: Helvetica, Arial, sans-serif;
  }

  .modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 40%;
    height: 40%;
    background-color: rgba(0, 0, 0, .5);
    display: table;
    transition: opacity .3s ease;
  }

  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }

  .btn-close {
    border: none;
    font-size: 20px;
    padding: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

  .btn-green {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
    align-content: center;
  }
</style>
