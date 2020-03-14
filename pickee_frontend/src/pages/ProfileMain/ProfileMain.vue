<template>
    <v-app>
        <v-navigation-drawer> 
            
        </v-navigation-drawer>

        <div class="page-wrapper profile-page">
            <PageHeader />
        </div>
      
    </v-app>
</template>

<script>
import PageHeader from "@/components/PageHeader/PageHeader.vue";

export default {
    name: "ProfileMain",
    data: function() {
        return {};
    },

    components: { PageHeader }
};
</script>