<template>
  <div>
    <!-- <v-form ref="form" v-model="invalid" lazy-validation> -->
    <v-text-field v-model="jobTitle" label="Job Title" @keyup="checkValid" required></v-text-field>
    <v-text-field v-model="companyProfile" label="Company profile" @keyup="checkValid" required></v-text-field>
    <v-text-field v-model="jobDescription" label="Job Description" @keyup="checkValid" required></v-text-field>
    <v-text-field v-model="jobRequirements" label="Job Requirements" @keyup="checkValid" required></v-text-field>
    <v-text-field v-model="jobBenefits" label="Job Benefits" @keyup="checkValid" required></v-text-field>

    <v-btn :disabled="invalid" color="success" style="width: 50%; margin-left: 25%;" @click="submit">
      Submit
    </v-btn>
    <!-- <v-select
      v-model="select"
      :items="items"
      :rules="[v => !!v || 'Item is required']"
      label="Item"
      required
    ></v-select>

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'You must agree to continue!']"
      label="Do you agree?"
      required
    ></v-checkbox> -->
    <!-- </v-form> -->
  </div>
</template>

<script>
export default {
  data: () => ({
    invalid: true,
    jobTitle: "",
    companyProfile: "",
    jobDescription: "",
    jobRequirements: "",
    jobBenefits: "",
    // checkbox: false,
  }),

  methods: {
    submit() {
      // this.$refs.form.validate()
    },
    checkValid() {
      if (
        this.jobTitle.trim() == "" || //this.jobTitle == null ||
        this.companyProfile.trim() == "" || //this.companyProfile == null ||
        this.jobDescription.trim() == "" || //this.jobDescription == null ||
        this.jobRequirements.trim() == "" || //this.jobRequirements == null ||
        this.jobBenefits.trim() == ""// || //this.jobBenefits == null
      ) {
        this.invalid = true
      } else {
        this.invalid = false
      }
    }
  },
}
</script>