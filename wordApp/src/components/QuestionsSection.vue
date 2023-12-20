<template>
  <v-container>
    <v-card class="mb-3" v-if="!finished">
      <v-card-title >{{ currentQuestion.sentence }}</v-card-title>
      <!-- <h1> {{ currentQuestion.results.selectedOption }} </h1> -->
      <v-card-text>
        <v-container>
          <v-row>
            <v-col v-for="(option, index) in currentQuestion.options" :key="index" cols="12" sm="6">
              <v-btn block color="primary" style="text-transform: none;" @click="selectOption(option)">
                {{ option }}
              </v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>
    <div v-else>
      <v-row justify="center">
        <v-col cols="12" sm="8" md="6">
          <v-card class="text-center">
            <v-card-title class="headline">
              Quiz Completed!
            </v-card-title>
            <v-card-text>
              <p>Thank you for participating in our quiz. Your responses have been recorded.</p>
              <p>If you have any more questions or would like to take another quiz, feel free to explore more.</p>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" @click="goToHomePage">
                Go to Home
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    
    </div>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'QuestionsSection',
  props: {
    questions: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      currentQuestionIndex: 0,
      startTime: Date.now(),
      finished: false,
    };
  },
  computed: {
    currentQuestion() {
      try {
        console.log('Current question: ', this.questions[this.currentQuestionIndex]);
        return this.questions[this.currentQuestionIndex];
      } catch (error) {
        console.error('Error fetching data:', error);
      }
      // if (this.currentQuestionIndex < this.questions.length) {
      //   return this.questions[this.currentQuestionIndex];
      // }
      // return null;
    }
  }, 
  methods: {
    selectOption(option) {
      const endTime = Date.now();
      let timeTaken = (endTime - this.startTime) / 1000; // Time in seconds
      console.log('Time taken:', timeTaken);
      console.log('Selected option:', option);
      timeTaken = JSON.stringify(timeTaken);

      this.questions[this.currentQuestionIndex].results.selectedOption = option;
      this.questions[this.currentQuestionIndex].results.time = timeTaken;

      this.saveProgess();

      this.moveToNextQuestion();
    },
    async moveToNextQuestion() {
      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.currentQuestionIndex++;
        this.startTime = Date.now(); // Reset timer for next question
      } else {
        // All questions are answered
        this.finished = true;
        console.log('Quiz completed');
        // Additional logic for end of quiz can be implemented here

        // get data from cookies UserData
        const userData = this.$cookies.get('userData');
        const results = {
          user: userData,
          results: this.questions
        };
        console.log('Results: ', results);
        await axios.post('http://localhost:8000/results', results).then((response) => {
              console.log(response);
            }, (error) => {
              console.log(error);
            });
        // console.this.questions = response.data.questions; // Store the response data in your component
        console.log('QUestions Game comp: ', this.questions)
      }
    },
    saveProgess() {
      // Save progress to database
      console.log('Saving progress...');
      // const progress = {
      //   currentQuestionIndex: this.currentQuestionIndex,
      //   questions: this.questions
      // };
      // this.$cookies.set('quizProgress', JSON.stringify(progress), '1d');
    },
    loadProgress() {
      // const progress = this.$cookies.get('quizProgress');
      // if (progress) {
      //   const savedData = JSON.parse(progress);
      //   this.currentQuestionIndex = savedData.currentQuestionIndex;
      //   this.questions = savedData.questions;
      //   this.startTime = Date.now(); // Reset start time
      // }
    }
  }
};
</script>