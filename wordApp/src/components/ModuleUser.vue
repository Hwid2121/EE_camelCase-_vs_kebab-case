<template>
  <v-container>
    <v-form @submit.prevent="submitForm">
      <!-- Gender Field with Tooltip -->
      <div class="d-flex align-center">
        <v-select
          v-model="userData.gender"
          :items="['Male', 'Female', 'Other']"
          label="Gender"
          required
        ></v-select>
      </div>

      <!-- Age Field with Tooltip -->
      <div class="d-flex align-center">
        <v-text-field
          v-model="userData.age"
          label="Age"
          type="number"
          required
        ></v-text-field>
      </div>

      <!-- IT Skills Checkbox with Tooltip -->
      <div class="d-flex align-center">
        <v-checkbox v-model="userData.hasItSkills" label="Do you have IT skills?"></v-checkbox>
        <v-tooltip text="The search engine is optimized for world of photography and tips and tricks on that.">
          <template v-slot:activator="{ props }">
            <v-chip v-bind="props" prepend-icon="mdi-information">
              Why?
            </v-chip>
          </template>
        </v-tooltip> 
      </div>

      <!-- Glasses Usage Checkbox with Tooltip -->
      <div class="d-flex align-center">
        <v-checkbox v-model="userData.usesGlasses" label="Do you use glasses?"></v-checkbox>
        <v-tooltip text="The search engine is optimized for world of photography and tips and tricks on that.">
          <template v-slot:activator="{ props }">
            <v-chip v-bind="props" prepend-icon="mdi-information">
              Why?
            </v-chip>
          </template>
        </v-tooltip> 
      </div>

      <!-- Data Consent Checkbox with Tooltip -->
      <div class="d-flex align-center">
        <v-checkbox v-model="userData.consent" label="I confirm the submission of my data for the experiment" required></v-checkbox>
        <v-tooltip text="The search engine is optimized for world of photography and tips and tricks on that.">
          <template v-slot:activator="{ props }">
            <v-chip v-bind="props" prepend-icon="mdi-information">
              Why?
            </v-chip>
          </template>
        </v-tooltip> 
      </div>

      <v-btn type="submit" color="primary" :disabled="!userData.consent">Submit & Start Game</v-btn>
    </v-form>
  </v-container>
</template>

<script>
export default {
  name: 'ModuleUser',
  data() {
    return {
      userData: {
        gender: '',
        age: null,
        hasItSkills: false,
        usesGlasses: false,
        consent: false
      },
    };
  },
  methods: {
    submitForm() {
      console.log('Form Data:', this.userData);
      this.$cookies.set('userData', this.userData);
      this.$router.push('/game');
    }
  }
};
</script>

<style>

</style>