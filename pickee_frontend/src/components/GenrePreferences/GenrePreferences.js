export default {
    name: "GenrePreferences",
    props: ["changeEvent", "items", "selected"],
    data: function() {
        return {
            select: this.selected
        }
    },
    watch: {
        select() {
            this.$emit('input', this.select);
        }
    }
};
