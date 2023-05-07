<template>
  <v-container>
    <v-row>
      <v-col cols="4">
        <v-checkbox @change="checkValid" v-model="disableJobTitle" label="Do you want to add the job title?"></v-checkbox>
        <v-textarea v-if="disableJobTitle" v-model="jobTitle" label="Job Title" @keyup="checkValid" required></v-textarea>
      </v-col>
      <v-col cols="4">
        <v-checkbox @change="checkValid" v-model="disableCompanyProfile"
          label="Do you want to add the company profile?"></v-checkbox>
        <v-textarea v-if="disableCompanyProfile" v-model="companyProfile" label="Company profile" @keyup="checkValid"
          required></v-textarea>
      </v-col>
      <v-col cols="4">
        <v-checkbox @change="checkValid" v-model="disableJobDescription"
          label="Do you want to add the job description?"></v-checkbox>
        <v-textarea v-if="disableJobDescription" v-model="jobDescription" label="Job Description" @keyup="checkValid"
          required></v-textarea>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6">
        <v-checkbox @change="checkValid" v-model="disableJobRequirements"
          label="Do you want to add the job requirements?"></v-checkbox>
        <v-textarea v-if="disableJobRequirements" v-model="jobRequirements" label="Job Requirements" @keyup="checkValid"
          required></v-textarea>
      </v-col>
      <v-col cols="6">
        <v-checkbox @change="checkValid" v-model="disableJobBenefits"
          label="Do you want to add the job benefits?"></v-checkbox>
        <v-textarea v-if="disableJobBenefits" v-model="jobBenefits" label="Job Benefits" @keyup="checkValid"
          required></v-textarea>
      </v-col>
    </v-row>
    <v-btn :disabled="invalid" color="success" style="width: 50%; margin-left: 25%;" @click="submit">
      Submit
    </v-btn>
    <div v-if="result != ''">
      <v-divider class="mt-8"></v-divider>
      <v-alert dense v-if="result.prediction == 'Neutral'" type="info">
        The model <strong>had low confidence!</strong> Enter more relevant data.
      </v-alert>
      <v-alert dense v-else-if="result.prediction == 'Positive'" type="error">
        This is a <strong>fake job!</strong>
      </v-alert>
      <v-alert dense v-else type="success">
        This is a <strong>real job!</strong>
      </v-alert>
    </div>
  </v-container>
</template>

<script>

import { predictJob } from "../utils/api";
export default {
  data: () => ({
    disableJobTitle: false,
    disableCompanyProfile: false,
    disableJobDescription: false,
    disableJobRequirements: false,
    disableJobBenefits: false,
    invalid: true,
    jobTitle: "",
    companyProfile: "",
    jobDescription: "",
    jobRequirements: "",
    jobBenefits: "",
    result: ""
  }),

  methods: {
    async submit() {
      if (
        this.jobTitle.trim() == "" &&
        this.companyProfile.trim() == "" &&
        this.jobDescription.trim() == "" &&
        this.jobRequirements.trim() == "" &&
        this.jobBenefits.trim() == ""
      ) {
        return
      } else {
        const predictionResponse = await predictJob({
          "job_title": this.jobTitle,
          "company_profile": this.companyProfile,
          "job_description": this.jobDescription,
          "job_requirements": this.jobRequirements,
          "job_benefits": this.jobBenefits
        })
        this.result = predictionResponse.data
        this.disableJobTitle = false
        this.disableCompanyProfile = false
        this.disableJobDescription = false
        this.disableJobRequirements = false
        this.disableJobBenefits = false
        this.jobTitle = ""
        this.companyProfile = ""
        this.jobDescription = ""
        this.jobRequirements = ""
        this.jobBenefits = ""
      }

    },
    checkValid() {
      if (
        !this.disableJobTitle &&
        !this.disableCompanyProfile &&
        !this.disableJobDescription &&
        !this.disableJobRequirements &&
        !this.disableJobBenefits
      ) {
        this.invalid = true
        return
      }
      if (
        this.disableJobTitle && this.jobTitle.trim() == "") {
        this.invalid = true
        return
      }
      if (
        this.disableCompanyProfile && this.companyProfile.trim() == "") {
        this.invalid = true
        return
      }
      if (
        this.disableJobDescription && this.jobDescription.trim() == "") {
        this.invalid = true
        return
      }
      if (
        this.disableJobRequirements && this.jobRequirements.trim() == "") {
        this.invalid = true
        return
      }
      if (
        this.disableJobBenefits && this.jobBenefits.trim() == "") {
        this.invalid = true
        return
      }
      this.invalid = false
    }
  },
}
</script>