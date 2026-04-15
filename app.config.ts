export default defineAppConfig({
  ui: {
    colors: {
      primary: 'amber',
      secondary: 'emerald',
      neutral: 'stone',
      info: 'sky',
      success: 'emerald',
      warning: 'amber',
      error: 'rose'
    },
    icons: {
      search: 'i-lucide-search',
      loading: 'i-lucide-loader-circle',
      close: 'i-lucide-x',
      external: 'i-lucide-arrow-up-right',
      chevronDown: 'i-lucide-chevron-down',
      chevronRight: 'i-lucide-chevron-right',
      arrowLeft: 'i-lucide-arrow-left',
      arrowRight: 'i-lucide-arrow-right',
      dark: 'i-lucide-moon-star',
      light: 'i-lucide-sun-medium',
      system: 'i-lucide-monitor'
    },
    button: {
      defaultVariants: {
        color: 'neutral',
        variant: 'outline'
      }
    },
    card: {
      defaultVariants: {
        variant: 'outline'
      }
    }
  }
})

