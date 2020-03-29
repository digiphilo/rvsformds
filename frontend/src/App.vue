<template>
  <div id="app">
    <div><Banner/></div>
    <div class="container" v-if="appData.formIsSent"><Sent/></div>
    <div class="container" v-if="!appData.formIsSent">
      <div class="row">
        <div class="col-sm"><Owner @formSent="onFormSent"/></div>
        <div class="col-sm"><Medic @formSent="onFormSent"/></div>
      </div>
    </div>
  </div>
</template>

<script>
import Banner from './components/Banner.vue'
import Owner from './components/Owner.vue'
import Medic from './components/Medic.vue'
import Sent from './components/Sent.vue'

export default {
  name: 'App',
  components: {
    Banner, Owner, Medic, Sent
  },
  data() {
    return {
      appData: {
          formIsSent: false
      }
    }
  },
  methods: {
    onFormSent: function() {
      this.appData.formIsSent = true
    }
  }
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 40px;
}
.logo {
  margin-bottom: 40px;
}
</style>
