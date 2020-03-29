<template>
  <div class="owner">
    <h2>RV Owner</h2>
    <div class="form-group">
      <label for="name">Name</label>
      <input type="text"
              id="email"
              class="form-control"
              v-model="ownerData.name">
      <label for="email">Email Address</label>
      <input type="email"
              id="email"
              class="form-control"
              v-model="ownerData.email">
      <label for="email">Phone Number</label>
      <input type="tel"
              id="telephone"
              class="form-control"
              v-model="ownerData.phone">
      <label for="city">City</label>
      <input type="text"
              id="city"
              class="form-control"
              v-model="ownerData.city">
      <label for="county">County</label>
      <input type="text"
              id="county"
              class="form-control"
              v-model="ownerData.county">
      <label for="state">State</label>
      <input type="text"
              id="state"
              class="form-control"
              v-model="ownerData.state">
      <label for="state">Zip Code</label>
      <input type="text"
              id="zip"
              class="form-control"
              v-model="ownerData.zip">
      <label for="rvtype">RV Type</label>
              <input type="text"
                      id="rvtype"
                      class="form-control"
                      v-model="ownerData.rvtype">
      <label for="other">Other Details</label>
      <textarea class="form-control" id="other" rows="3" v-model="ownerData.other"></textarea>
      <label for="btn"></label>
      <button type="button" class="btn btn-success btn-block" v-on:click="submit">Submit</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Owner',
  data() {
    return {
      ownerData: {}
    }
  },
  methods: {
    submit: function() {
      this.$emit('formSent')
      this.axios.post('https://rvapi.herokuapp.com/owner_form',
      {
        'name': this.ownerData.name,
        'email': this.ownerData.email,
        'phone': this.ownerData.phone,
        'city': this.ownerData.city,
        'state': this.ownerData.state,
        'county': this.ownerData.county,
        'zip': this.ownerData.zip,
        'rvtype': this.ownerData.rvtype,
        'other': this.ownerData.other
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
