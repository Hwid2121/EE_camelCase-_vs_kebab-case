<template>
    <v-container>
        <info-page/>
      <ModuleUser/>
    </v-container>
  </template>
  
  <script>
  import QuestionsSection from '@/components/QuestionsSection.vue'
  import ModuleUser from '@/components/ModuleUser.vue'
  import InfoPage from '@/components/InfoPage.vue'
  
  export default {
    name: 'MainPage',
    components: {
      QuestionsSection,
      ModuleUser,
      InfoPage
    }
  }
  </script>
  