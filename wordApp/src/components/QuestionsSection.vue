<template>
    <v-container>
      <v-card class="mb-3">
        <v-card-title>{{ question }}</v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col v-for="(option, index) in options" :key="index" cols="12" sm="6">
                <v-btn block color="primary" @click="selectOption(option)">
                  {{ option }}
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    name: 'QuestionsSection',
    data() {
    return {
        question: 'Your Word',
      options: ['Option1', 'Option2', 'Option3', 'Option4'],
      timer: 0,
      startTime: null,
      intervalId: null,
    };
  },
  mounted() {
    this.startTime = Date.now();
    this.intervalId = setInterval(this.updateTimer, 1000);
  },
    methods: {
      selectOption(option) {
        console.log('Selected Option:', option);
      }
    }
  };
  </script>
  
  <style>
  /* Add any additional styles here */
  </style>
  