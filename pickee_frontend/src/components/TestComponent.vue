<template>
    <v-combobox
        v-model="select"
        :items="items"
        label="Combobox"
        multiple
        chips
    ></v-combobox>
</template>

<script>
    export default {
        name: "TestComponent",
        data: () => ({
            select: ["Vuetify", "Programming"],
            items: ["Programming", "Design", "Vue", "Vuetify"]
        })
    };
</script>

<style scoped></style>
