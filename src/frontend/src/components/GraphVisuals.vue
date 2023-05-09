<!--
  Shows graphs on the Visualizations tab
  Used ApexCharts library to achieve this
-->
<template>
  <v-container>
    <v-row>
      <v-col cols="6">
        <p class="text-h3 my-16"> Variation in required experiences</p>
      </v-col>
      <v-col cols="6">
        <apex-chart width="100%" type="pie" :options="experienceChartOptions" :series="experiencesNumbers"></apex-chart>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6">
        <p class="text-h3 my-16"> Top countries in the database</p>
      </v-col>
      <v-col cols="6">
        <apex-chart width="100%" type="bar" :options="countryChartOptions" :series="countryNumbers"></apex-chart>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6">
        <p class="text-h3 my-16"> Ratio of fake and real jobs</p>
      </v-col>
      <v-col cols="6">
        <apex-chart width="100%" type="donut" :options="fraudulentChartOptions" :series="fraudulentNumbers"></apex-chart>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6">
        <p class="text-h3 my-16"> Top required experiences in the database</p>
      </v-col>
      <v-col cols="6">
        <apex-chart width="100%" type="bar" :options="educationChartOptions" :series="educationNumbers"></apex-chart>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {
  // variables used in creating the charts
  data: () => ({
    experiencesNumbers: [4153, 2872, 1842, 2184, 724, 99, 297, 201],
    experienceChartOptions: {
      labels: ['not provided', 'mid senior level', 'associate', 'entry level', 'not applicable', 'executive', 'director', 'internship']
    },
    fraudulentNumbers: [11769, 603],
    fraudulentChartOptions: {
      labels: ['real', 'fake'],
    },
    countryNumbers: [{
      data: [{
        x: 'United States',
        y: 4236
      }, {
        x: 'Great Britain',
        y: 1397
      }, {
        x: 'Greece',
        y: 669
      }, {
        x: 'Canada',
        y: 392
      }, {
        x: 'Denmark',
        y: 285
      }, {
        x: 'New Zealand',
        y: 240
      }]
    }],
    countryChartOptions: {
      bar: {
        horizontal: true
      },
      fill: {
        colors: ['#357103']
      }
    },
    educationNumbers: [{
      data: [{
        x: 'Associate Degree',
        y: 237
      }, {
        x: 'High School',
        y: 1686
      }, {
        x: 'Bachelor\'s Degree',
        y: 4128
      }, {
        x: 'Master\'s Degree',
        y: 314
      }, {
        x: 'Doctorate',
        y: 190
      }, {
        x: 'Not provided',
        y: 4660
      }]
    }],
    educationChartOptions: {
      bar: {
        horizontal: true
      },
      fill: {
        colors: ['#934812']
      }
    },
  }),
}
</script>