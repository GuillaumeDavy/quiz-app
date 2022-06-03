<template>
  <!-- Modal -->
  <div class="modal-backdrop">
    <div class="modal modal-lg">
      <header class="modal-header">
        <slot name="header">
          {{ question ? 'Modifier la question' : modalTitle }}
        </slot>
        <button
          type="button"
          class="btn-close"
          @click="close"
        >
          x
        </button>
      </header>

      <section class="modal-body">
        <slot name="body">
          <div class="form">
            <div class="form-group">
              <label for="questionTitle">Titre de la question</label>
              <input type="text" class="form-control" id="questionTitle" placeholder="Ici le titre de la question" v-model="questionTitle">
            </div>
            <ImageUpload @file-change="imageFileChangedHandler" />

          </div>
          
        </slot>
       </section>

      <footer class="modal-footer">
        <slot name="footer">
          This is the default footer!
        </slot>
        <button
          type="button"
          class="btn-green"
          @click="close"
        >
          Close Modal
        </button>
      </footer>
    </div>
  </div>
</template>

<script>
import ImageUpload from '../components/ImageUpload.vue';
export default {
  name: "QuestionModal",
  data() {
    return {
      questionTitle: '',
      questionText : '',
      questionImage : null,
      modalTitle : 'Ajouter une question',
    };
  },
  emits: ['edit'],
  methods: {
    close() {
      this.$emit('close');
    },
    imageFileChangedHandler(b64String) {
      this.image = b64String;
    },
    updateQuestion(question){
      if(question){
        this.questionTitle = question.title;
        this.questionText = question.text;
        this.questionImage = question.image;
        this.modalTitle = 'Modifier une question';
        console.log(this.questionTitle);
      }
    }
  },
  components: {
    ImageUpload
  },
  props: {
    question: {
      type: Object
    }
  },
  async created() {
		console.log("Question Modal");
  }
};
</script>

<style>
  .modal-backdrop {
    position: fixed;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: hidden;
    display: flex;
    flex-direction: column;
  }

  .modal-lg{
    height: 50%;
    left: auto;
    top: auto;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    flex-direction: column;
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }

  .btn-close {
    position: absolute;
    top: 0;
    right: 0;
    border: none;
    font-size: 20px;
    padding: 10px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

  .btn-green {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
  }
</style>