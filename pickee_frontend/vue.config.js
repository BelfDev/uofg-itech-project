const BundleTracker = require("webpack-bundle-tracker");
const VuetifyLoaderPlugin = require("vuetify-loader/lib/plugin");

const pagesList = [
    "_Demo",
    "Home",
    "Login",
    "SignUp",
    "About",
    "Profile",
    "History",
    "Preferences",
    "Recommendation"
];

let pages = {};

pagesList.forEach(pageName => {
    pages[pageName] = {
        entry: `./src/pages/${pageName}/${pageName}`,
        chunks: ["chunk-vendors"]
    };
});

module.exports = {
    pages: pages,
    filenameHashing: false,
    productionSourceMap: false,
    publicPath:
        process.env.NODE_ENV === "production" ? "" : "http://localhost:8080/",
    outputDir: "../pickee_project/static/vue/",

    chainWebpack: config => {
        config.optimization.splitChunks({
            cacheGroups: {
                vendor: {
                    test: /[\\/]node_modules[\\/]/,
                    name: "chunk-vendors",
                    chunks: "all",
                    priority: 1
                }
            }
        });

        Object.keys(pages).forEach(page => {
            config.plugins.delete(`html-${page}`);
            config.plugins.delete(`preload-${page}`);
            config.plugins.delete(`prefetch-${page}`);
        });

        config
            .plugin("BundleTracker")
            .use(BundleTracker, [
                { filename: "../pickee_frontend/webpack-stats.json" }
            ]);

        config.plugin("VuetifyLoaderPlugin").use(VuetifyLoaderPlugin);

        config.resolve.alias.set("__STATIC__", "static");

        config.devServer
            .public("http://localhost:8080")
            .host("localhost")
            .port(8080)
            .hotOnly(true)
            .watchOptions({ poll: 1000 })
            .https(false)
            .headers({ "Access-Control-Allow-Origin": ["*"] });
    }
};
