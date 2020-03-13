import FormTextField from "@/components/FormTextField/FormTextField.vue";

export default {
    name: "LoginBox",
    data: function() {
        return {
            token: this.$cookies.get("csrftoken")
        }
    },
    props: ['formUrl'],
    components: {
        FormTextField
    }
}
