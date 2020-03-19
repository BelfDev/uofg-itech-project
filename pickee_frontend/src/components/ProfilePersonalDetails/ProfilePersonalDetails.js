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
    data: () => ({
        genderDropdownItems: [] // TODO: get from API
    }),
    components: {
        FormDropdownField
    }
}