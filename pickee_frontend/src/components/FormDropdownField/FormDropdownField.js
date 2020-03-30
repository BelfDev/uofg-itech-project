export default {
    name: "FormDropdownField",
    props: ["label", "name", "title", "items", "value", "changeEvent"],
    data: function() {
        return {
            model: this.value
        }
    },
    watch: {
        select() {
            this.$emit("input", this.select);
        }
    }
};
