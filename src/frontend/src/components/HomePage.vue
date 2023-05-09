<template>
  <v-container>
    <v-alert class="my-16 text-justify text-h4" color="blue" dense text elevation="2">
      Welcome to <strong>Job Verify!</strong> <br>
      This tool assists users in classifying the authenticity of a job posting. It prevents them from being scammed by fake
      job poster agencies and saves them from sharing sensitive information to illegitimate parties.<br>
      To use the tool, enter relevant details below to get prediction on whether this is a real or a fake job.<br>
      You can also see some graphs in the visualizations tab. To go the tab, click the visualizations button on the top right. The graphs are interactive so feel free to hover and click on elements.
    </v-alert>
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
        this.invalid = true
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