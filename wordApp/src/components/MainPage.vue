<template>
    <v-container>
      <QuestionsSection/>
    </v-container>
  </template>
  
  <script>
  import QuestionsSection from '@/components/QuestionsSection.vue'
  
  export default {
    name: 'MainPage',
    components: {
      QuestionsSection
    }
  }
  </script>
  