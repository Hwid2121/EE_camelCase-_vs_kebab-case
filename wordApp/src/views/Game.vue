<template>
    <QuestionsSection />
  </template>
  
  <script>
    import QuestionsSection from '@/components/QuestionsSection.vue'
    import axios from 'axios';

  export default {
    name: 'Game',
    data() {
      return {
        questions: [], // This will hold your questions data
      };
    },
    created() {
      this.fetchQuestions();
    },
    methods: {
      async fetchQuestions() {
        try {
        const response = await axios.get('http://localhost:8000/questions'); 
        this.data = response.data; // Store the response data in your component
        console.log('Questions:', this.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
      }
    }
  };
  </script>
  