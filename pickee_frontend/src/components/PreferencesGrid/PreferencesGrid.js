import AddItemDialog from "@/components/AddItemDialog/AddItemDialog.vue";

export default {
    name: "PreferencesGrid",
    props: [
        "items",
        "entries",
        "type",
        "addMethod",
        "addButtonText",
        "boxTitle",
        "removeMethod",
        "searchMethod",
        "saveMethod",
        "searchLoading",
    ],
    components: {
        AddItemDialog
    }
};
