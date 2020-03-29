export default {
    props: ['name'],
    computed: {
        timePretty: function() {
            let text;
            const mins = this.minutes;

            if (mins < 60) {
                text = `${mins} minutes`;
            } else {
                const h = mins / 60;
                const pl = h > 1 ? "s" : "";
                text = `${h} hour${pl}`;
            }
            return text;
        }
    },
    data: () => ({
        minutes: 120
    })
};
