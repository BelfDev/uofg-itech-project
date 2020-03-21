import FormDropdownField from "@/components/FormDropdownField/FormDropdownField.vue";

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
    data: () => ({
        genderDropdownItems: ['MALE', 'FEMALE', 'OTHER', 'UNSPECIFIED'] // TODO: get from API
    }),
    components: {
        FormDropdownField
    }
}