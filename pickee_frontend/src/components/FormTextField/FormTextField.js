export default {
    name: "FormTextField",
    props: {
        label: String,
        name: String,
        type: String,
        placeholder: String,
        horizontal: Boolean,
        value: String,
        changeEvent: Function
    },
    data: function() {
        return {
            model: this.value
        }
    },
    watch: {
        model() {
            this.$emit("input", this.model);
        }
    }
};
