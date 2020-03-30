import FormDropdownField from "@/components/FormDropdownField/FormDropdownField.vue";
import FormTextField from "@/components/FormTextField/FormTextField.vue";

export default {
    name: "ProfilePersonalDetails",
    computed: {
        ageDropdownItems: () => {
            const ageArray = []; 
            for (let i = 1; i < 100; i++) {
                ageArray.push(i);
            }
            return ageArray;
        }
    },
    props: ['user', 'updatePersonalDetails'],
    data: function() {
        return {
            genderDropdownItems: ['MALE', 'FEMALE', 'OTHER', 'UNSPECIFIED'],
            first_name: this.user.first_name,
            last_name: this.user.last_name,
        }
    },
    components: {
        FormDropdownField,
        FormTextField
    }
}