<template>
  <div class="medic">
    <h2>Care Provider</h2>
    <div class="form-group">
      <label for="name">Name</label>
      <input type="text"
              id="name"
              class="form-control"
              v-model="medicData.name">
      <label for="email">Email Address</label>
      <input type="email"
              id="email"
              class="form-control"
              v-model="medicData.email">
      <label for="email">Phone Number</label>
      <input type="tel"
              id="phone"
              class="form-control"
              v-model="medicData.phone">
      <label for="city">City</label>
      <input type="text"
              id="city"
              class="form-control"
              v-model="medicData.city">
      <label for="county">County</label>
      <input type="text"
              id="county"
              class="form-control"
              v-model="medicData.county">
      <label for="state">State</label>
      <input type="text"
              id="state"
              class="form-control"
              v-model="medicData.state">
      <label for="state">Zip Code</label>
      <input type="text"
              id="zip"
              class="form-control"
              v-model="medicData.zip">
      <label for="other">Other Details</label>
      <textarea class="form-control" id="other" rows="3" v-model="medicData.other"></textarea>
      <label for="btn"></label>
      <button type="button" class="btn btn-success btn-block" v-on:click="submit">Submit</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Medic',
  data() {
    return {
      medicData: {}
    }
  },
  methods: {
    submit: function() {
      this.$emit('formSent')
      this.axios.post('https://rvapi.herokuapp.com//medic_form',
      {
        'name': this.medicData.name,
        'email': this.medicData.email,
        'phone': this.medicData.phone,
        'city': this.medicData.city,
        'state': this.medicData.state,
        'county': this.medicData.county,
        'zip': this.medicData.zip,
        'other': this.medicData.other
      }).then(response => console.log(response));
    }
  }
}
</script>

<style scoped>
h2 {
  margin: 40px 0 0;
}
label {
  margin-top: 10px;
}
</style>
