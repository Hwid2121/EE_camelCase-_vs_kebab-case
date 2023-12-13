<template>
  <div>
    <QuestionsSection v-if="!loading" :questions="questions" />
      <span v-else>Loading!</span>
  </div>
</template>

<script>
import QuestionsSection from '@/components/QuestionsSection.vue';
import axios from 'axios';

export default {
  name: 'Game',
  components: {
    QuestionsSection,
  },
  data() {
    return {
      questions: {
        type: Array,
        required: true
      }, 
      loading: true,
    };
  },
  mounted() {
    console.log('Game mounted');
    this.fetchQuestions();
  },
  methods: {
    async fetchQuestions() {
      this.loading = true;
      try {
        console.log('Fetching questions');
        const response = await axios.get('http://localhost:8000/questions');
        this.questions = response.data.questions; // Store the response data in your component
        console.log('QUestions Game comp: ', this.questions)
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>
